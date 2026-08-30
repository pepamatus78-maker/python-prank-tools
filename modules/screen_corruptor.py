"""
Screen Corruptor Module

Create glitch and corruption effects on images.

EXAMPLE:
    from modules.screen_corruptor import ScreenCorruptor
    from PIL import Image
    
    corruptor = ScreenCorruptor()
    image = Image.open("screenshot.png")
    corrupted = corruptor.corrupt(image, intensity=0.5)
    corrupted.show()
"""

from PIL import Image, ImageEnhance, ImageFilter
import random


class ScreenCorruptor:
    """
    Create visual glitch and corruption effects.
    
    This class applies various corruption effects to images including:
    - RGB channel separation
    - Screen tearing
    - Pixel shifting
    - Melting effects
    - Blur and contrast manipulation
    """
    
    @staticmethod
    def rgb_channel_shift(image, intensity):
        """
        Separate and shift RGB channels.
        
        Args:
            image: PIL Image object
            intensity (float): Effect intensity (0-1)
            
        Returns:
            PIL Image: Image with shifted RGB channels
        """
        r, g, b = image.split()
        w, h = image.size
        
        shift = int(random.randint(2, 25) * intensity)
        
        r = r.transform(
            (w, h),
            Image.AFFINE,
            (1, 0, shift, 0, 1, 0)
        )
        
        b = b.transform(
            (w, h),
            Image.AFFINE,
            (1, 0, -shift, 0, 1, 0)
        )
        
        return Image.merge("RGB", (r, g, b))
    
    @staticmethod
    def screen_tear(image, intensity):
        """
        Create horizontal screen tearing effect.
        
        Args:
            image: PIL Image object
            intensity (float): Effect intensity (0-1)
            
        Returns:
            PIL Image: Image with screen tear
        """
        img = image.copy()
        w, h = img.size
        
        tears = int(15 + intensity * 150)
        
        for _ in range(tears):
            y = random.randint(0, max(1, h - 2))
            height = random.randint(1, max(2, int(3 + intensity * 30)))
            height = min(height, h - y)
            
            strip = img.crop((0, y, w, y + height))
            offset = random.randint(
                -int(150 + intensity * 600),
                int(150 + intensity * 600)
            )
            
            img.paste(strip, (offset, y))
        
        return img
    
    @staticmethod
    def melt(image, intensity):
        """
        Create a melting effect.
        
        Args:
            image: PIL Image object
            intensity (float): Effect intensity (0-1)
            
        Returns:
            PIL Image: Image with melting effect
        """
        img = image.copy()
        w, h = img.size
        
        strips = int(20 + intensity * 150)
        
        for _ in range(strips):
            y = random.randint(0, max(0, h - 5))
            strip_height = random.randint(2, max(3, int(10 + intensity * 60)))
            strip_height = min(strip_height, h - y)
            
            if strip_height <= 0:
                continue
            
            strip = img.crop((0, y, w, y + strip_height))
            max_shift = int(10 + intensity * 220)
            x_shift = random.randint(-max_shift, max_shift)
            y_shift = random.randint(0, int(5 + intensity * 150))
            
            img.paste(
                strip,
                (x_shift, min(h - strip_height, y + y_shift))
            )
        
        return img
    
    @staticmethod
    def corrupt(image, intensity=0.5):
        """
        Apply all corruption effects to an image.
        
        Args:
            image: PIL Image object
            intensity (float): Effect intensity (0-1), default 0.5
            
        Returns:
            PIL Image: Corrupted image
            
        EXAMPLE:
            from PIL import Image
            from modules.screen_corruptor import ScreenCorruptor
            
            img = Image.open("screenshot.png")
            corruptor = ScreenCorruptor()
            corrupted = corruptor.corrupt(img, intensity=0.7)
            corrupted.save("corrupted.png")
        """
        img = image.copy().convert("RGB")
        
        # Apply effects in sequence
        img = ScreenCorruptor.rgb_channel_shift(img, intensity)
        img = ScreenCorruptor.melt(img, intensity)
        img = ScreenCorruptor.screen_tear(img, intensity)
        
        # Contrast adjustment
        if random.random() < 0.4:
            enhancer = ImageEnhance.Contrast(img)
            img = enhancer.enhance(
                random.uniform(1.0, 1.0 + intensity * 2)
            )
        
        # Blur
        if random.random() < (intensity * 0.3):
            img = img.filter(
                ImageFilter.GaussianBlur(random.uniform(0.5, 2.5))
            )
        
        return img


# Example usage
if __name__ == "__main__":
    print("Screen Corruptor Demo")
    print("Note: Requires a screenshot.png file")
    
    try:
        # Create a sample image
        img = Image.new("RGB", (800, 600), color="blue")
        
        corruptor = ScreenCorruptor()
        
        # Apply corruption
        corrupted = corruptor.corrupt(img, intensity=0.7)
        
        # Save result
        corrupted.save("corrupted_demo.png")
        print("Saved corrupted image to corrupted_demo.png")
        
    except Exception as e:
        print(f"Error: {e}")
