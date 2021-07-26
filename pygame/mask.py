

def from_surface(surf, threshold=None):
    """
    Creates a Mask from the given surface
    from_surface(Surface) -> Mask
    from_surface(Surface, threshold=127) -> Mask

    Creates a Mask object from the given surface by setting all the opaque pixels and not setting the transparent pixels.

    If the surface uses a color-key, then it is used to decide which bits in the resulting mask are set. All the pixels that are not equal to the color-key are set and the pixels equal to the color-key are not set.

    If a color-key is not used, then the alpha value of each pixel is used to decide which bits in the resulting mask are set. All the pixels that have an alpha value greater than the threshold parameter are set and the pixels with an alpha value less than or equal to the threshold are not set.
    Parameters:	

        surface (Surface) -- the surface to create the mask from
        threshold (int) -- (optional) the alpha threshold (default is 127) to compare with each surface pixel's alpha value, if the surface is color-keyed this parameter is ignored

    Returns:	

    a newly created Mask object from the given surface
    Return type:	
    Mask

    N.B.This function is used to create the masks for pygame.sprite.collide_mask()Collision detection between two sprites, using masks..
    """
    pass


def from_threshold(surf, color):
    """
    Creates a mask by thresholding Surfaces
    from_threshold(Surface, color) -> Mask
    from_threshold(Surface, color, threshold=(0, 0, 0, 255), othersurface=None, palette_colors=1) -> Mask
    
    This is a more featureful method of getting a Mask from a surface.

    If the optional othersurface is not used, all the pixels within the threshold of the color parameter are set in the resulting mask.

    If the optional othersurface is used, every pixel in the first surface that is within the threshold of the corresponding pixel in othersurface is set in the resulting mask.
    Parameters:	

    surface (Surface) -- the surface to create the mask from
    color (Color or int or tuple(int, int, int, [int]) or list[int, int, int, [int]]) -- color used to check if the surface's pixels are within the given threshold range, this parameter is ignored if the optional othersurface parameter is supplied
    threshold (Color or int or tuple(int, int, int, [int]) or list[int, int, int, [int]]) -- (optional) the threshold range used to check the difference between two colors (default is (0, 0, 0, 255))
    othersurface (Surface) -- (optional) used to check whether the pixels of the first surface are within the given threshold range of the pixels from this surface (default is None)
    palette_colors (int) -- (optional) indicates whether to use the palette colors or not, a nonzero value causes the palette colors to be used and a 0 causes them not to be used (default is 1)

    Returns	
    a newly created Mask object from the given surface
    Return type:	
    """
    pass


class Mask:
    """
    useful for fast pixel perfect collision detection. A mask uses 1 bit per-pixel to store which parts collide.
    """
    pass
