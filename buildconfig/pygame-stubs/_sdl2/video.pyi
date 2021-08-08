from _typeshed import NoneType
from typing import Union, Tuple, Iterable, Optional, Any, Generator, List

from pygame.surface import Surface
from pygame.rect import Rect
from pygame.math import Vector2
from pygame.color import Color

_ColorValue = Union[
    Color, str, Tuple[int, int, int], List[int], int, Tuple[int, int, int, int]
]

_CanBeRect = Union[
    Rect,
    Tuple[float, float, float, float],
    Tuple[Tuple[float, float], Tuple[float, float]],
    List[float],
    List[Vector2],
    Tuple[Vector2, Vector2],
    Iterable[Vector2],
]

WINDOWPOS_UNDEFINED: int
WINDOWPOS_CENTERED: int

MESSAGEBOX_ERROR: int
MESSAGEBOX_WARNING: int
MESSAGEBOX_INFORMATION: int

class RendererDriverInfo:
    name: str
    flags: int
    num_texture_formats: int
    max_texture_width: int
    max_texture_height: int

def get_drivers() -> Generator[RendererDriverInfo, None, None]: ...
def get_grabbed_window() -> Optional[Window]: ...
def messagebox(
    title: str,
    message: str,
    window: Optional[Window] = None,
    info: bool = False,
    warn: bool = False,
    error: bool = False,
    buttons: Tuple[str, ...] = ("OK",),
    return_button: int = 0,
    escape_button: int = 0,
) -> int: ...

class Window:
    def __init__(
        self,
        title: str = "pygame",
        size: Iterable[int, int] = (640, 480),
        position: Optional[Iterable[int, int]] = None,
        fullscreen: bool = False,
        fullscreen_desktop=False,
        **kwargs: Any
    ) -> None: ...
    grab: bool
    relative_mouse: bool
    def set_windowed(self) -> None: ...
    def set_fullscreen(self, desktop: bool = False) -> None: ...
    title: str
    def destroy(self) -> None: ...
    def hide(self) -> None: ...
    def show(self) -> None: ...
    def focus(self, input_only: bool = False) -> None: ...
    def restore(self) -> None: ...
    def maximize(self) -> None: ...
    def minimize(self) -> None: ...
    resizable: bool
    borderless: bool
    def set_icon(self, surface: Surface) -> None: ...
    id: int
    size: Iterable[int, int]
    position: Union[int, Iterable[int, int]]
    opacity: float
    brightness: float
    display_index: int
    def set_modal_for(Window) -> None: ...

class Texture:
    def __init__(
        self,
        renderer: Renderer,
        size: Iterable[int, int],
        static: bool = False,
        streaming: bool = False,
        target: bool = False,
    ) -> None: ...
    def from_surface(renderer: Renderer, surface: Surface) -> Texture: ...
    renderer: Renderer
    width: int
    height: int
    alpha: int
    blend_mode: int
    color: Color
    def get_rect(self, **kwargs: Any) -> Rect: ...
    def draw(
        self,
        srcrect: Optional[_CanBeRect] = None,
        dstrect: Optional[Union[_CanBeRect, Iterable[int, int]]] = None,
        angle: int = 0,
        origin: Optional[Iterable[int, int]] = None,
        flipX: bool = False,
        flipY: bool = False,
    ) -> None: ...
    def update(self, surface: Surface, area: Optional[_CanBeRect] = None) -> None: ...

class Image:
    def __init__(
        self,
        textureOrImage: Union[Texture, Image],
        srcrect: Optional[_CanBeRect] = None,
    ) -> None: ...
    def get_rect(self, **kwargs: Any) -> Rect: ...
    def draw(
        srcrect: Optional[_CanBeRect] = None, dstrect: Optional[_CanBeRect] = None
    ) -> None: ...
    angle: float
    origin: Optional[Iterable[float, float]]
    flipX: bool
    flipY: bool
    color: Color
    alpha: float
    blend_mode: int
    texture: Texture
    srcrect: Rect

class Renderer:
    def __init__(
        self,
        window: Window,
        index: int = -1,
        accelerated: int = -1,
        vsync: bool = False,
        target_texture: bool = False,
    ) -> None: ...
    def from_window(window: Window) -> Renderer: ...
    draw_blend_mode: int
    draw_color: Color
    def clear(self) -> None: ...
    def present(self) -> None: ...
    def get_viewport(self) -> Rect: ...
    def set_viewport(self, area: Optional[_CanBeRect]) -> None: ...
    logical_size: Iterable[int, int]
    scale: Iterable[float, float]
    target: Union[Texture, None]
    def blit(
        self,
        source: Union[Texture, Image],
        dest: Optional[_CanBeRect] = None,
        area: Optional[_CanBeRect] = None,
        special_flags: int = 0,
    ) -> Rect: ...
    def draw_line(self, p1: Iterable[int, int], p2: Iterable[int, int]) -> None: ...
    def draw_point(self, point: Iterable[int, int]) -> None: ...
    def draw_rect(self, rect: _CanBeRect) -> None: ...
    def fill_rect(self, rect: _CanBeRect) -> None: ...
    def to_surface(
        self, surface: Optional[Surface] = None, area: Optional[_CanBeRect] = None
    ) -> Surface: ...
