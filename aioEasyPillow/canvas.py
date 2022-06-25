"""
MIT License

Copyright (c) 2021-2022 shahriyardx
Copyright (c) 2022-present Guddi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from typing import Tuple, Union

from PIL import Image


class Canvas:
    """Canvas class

    Parameters
    ----------
    size : Tuple[float, float], optional
        Size of image, by default None
    width : float, optional
        Width of image, by default None
    height : float, optional
        Height of image, by default None
    color : Union[Tuple[int, int, int], str, int], optional
        Color of image, by default None

    Raises
    ------
    ValueError
        When either ``size`` or ``width and height`` is not a provided
    """

    def __init__(
        self,
        size: Tuple[float, float] = None,
        width: float = None,
        height: float = None,
        color: Union[Tuple[int, int, int], str, int] = None,
    ) -> None:
        if not size and not width and not height:
            raise ValueError("size, width, and height cannot all be None")

        if width and height:
            size = (width, height)

        self.size = size
        self.color = color

        self.image = Image.new("RGBA", size, color=color)
