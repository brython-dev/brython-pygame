from browser import console, document, html, window

from .rect import Rect
from . import base


_canvas_id = None


class Surface:

    _free_canvas_id = 1

    ref_to_mainsurface = None
    
    def __init__(self, size=None, depth=16, surf=None, jsimg=None):
        print('crea surface num.{}  - - {} {} {} {} '.format(Surface._free_canvas_id, size, depth, surf, jsimg))

        self._canvas = None
        self._js_image = None
        self._size = size
        self._chosen_colorkey = None

        if jsimg is not None:
            self._js_image = jsimg
            self._canvas = html.CANVAS(width=size[0], height=size[1])

        elif surf is None:
            self._canvas = html.CANVAS(width=size[0], height=size[1])
            self._depth = depth

        elif isinstance(surf, Surface):  # used by pygame.font.Font.render
            self._canvas = surf.canvas
            self._size = self._canvas.width, self._canvas.height

        elif isinstance(surf, html.CANVAS):  # TODO analysis: when this is used?
            self._canvas = surf
            self._size = surf.width, surf.height

        self._canvas.id = 'layer_%s' % Surface._free_canvas_id
        self.identifier = Surface._free_canvas_id
        Surface._free_canvas_id += 1

        if self.identifier == 1:
            Surface.ref_to_mainsurface = self

    def blit(self, sourcesurf, pos_dest, area=None, special_flags=0):
        #  TODO should we take @area, @special_flags parameters into account?

        if sourcesurf.imagetype:

            if sourcesurf.colorkey is None:
                self.context.drawImage(sourcesurf.jsimage, pos_dest[0], pos_dest[1])
            else:
                # (tom's hack) support of the colorkey feature

                sw, sh = sourcesurf.get_size()

                src_context = sourcesurf.context
                dst_context = self.context

                # src_context.clearRect(0, 0, sw, sh)
                src_context.drawImage(sourcesurf.jsimage, 0, 0)
                refdata = src_context.getImageData(0, 0, sw, sh)
                pixels = refdata.data

                ck_rv, ck_gv, ck_bv = sourcesurf.colorkey
                for k in range(sw*sh):
                    idxr = 4*k
                    idxg = idxr+1
                    idxb = idxr+2
                    idxalpha = idxr+3
                    if pixels[idxr] == ck_rv and pixels[idxg] == ck_gv and pixels[idxb] == ck_bv:
                        pixels[idxr] = None
                        pixels[idxg] = None
                        pixels[idxb] = None
                        pixels[idxalpha] = None

                dst_context.putImageData(refdata, pos_dest[0], pos_dest[1])

                # self._context.putImageData(_tmp_imgdata, pos_dest[0], pos_dest[1], 1, 1, bsup_x, bsup_y)
                # dst_context.drawImage(pixels, pos_dest[0], pos_dest[1])

        else:
            # the general case
            self.context.drawImage(sourcesurf.canvas, pos_dest[0], pos_dest[1])
        return
        
        # if area is None and isinstance(source, str):
        #   _img = JSConstructor(window.Image)()
        #   _img.src = source

        #   def img_onload(*args):
        #       self._context.drawImage(_img, dest[0], dest[1])

        #   _img.onload=img_onload
        #   _img.width, _img.height

        # global _canvas_id
        #
        # if _canvas_id is None:
        #     try:
        #         _canvas_id = document.get(selector='canvas')[0].getAttribute('id')
        #     except:
        #         pass
        #
        # if self._canvas.id == _canvas_id:
        #     self._canvas.width = self._canvas.width
        #
        # if area is None:
        #     # lets set area to the size of the source
        #     if isinstance(source, Surface):
        #         area = [(0, 0), (source.canvas.width, source.canvas.height)]
        #
        # if isinstance(source, Surface):
        #     _ctx = source.canvas.getContext('2d')
        #     _subset = _ctx.getImageData(area[0][0], area[0][1], area[1][0], area[1][1])
        #     contenu = _subset.data
            
##            # proc colorkey
##            for k in range(48*72):  # TODO dim pas en manuel!
##                tmpi = 4*k
##                tmpj = tmpi+1
##                tmpk = tmpi+2
##                tmpl = tmpi+3
##                if all((contenu[tmpi]==0xff, contenu[tmpj]==0x00, contenu[tmpk]==0xff)):
##                    contenu[tmpl] = 0
##                    contenu[tmpk] = contenu[tmpj] = contenu[tmpi] = 200  # TODO colorkey parametrabl

        # - -  -unreachable july21 (we want just a subset of the source image copied)
        # self._context.putImageData(_subset, dest[0], dest[1])
        # print(dest[0], dest[1], _subset.width, _subset.height)
        # return Rect(dest[0], dest[1], dest[0] + _subset.width, dest[1] + _subset.height)

    def convert_alpha(self):
        # TODO fix me...
        return self

    def convert(self, surface=None):
        # TODO fix me...
        return self

    def copy(self):
        args = [0, 0, self._canvas.width, self._canvas.height]
        _imgdata = self.context.getImageData(*args)  # toDataURL('image/png')

        _canvas = html.CANVAS(width=self._canvas.width, height=self._canvas.height)
        _ctx = _canvas.getContext('2d')
        # _ctx.drawImage(_imgdata, 0, 0)
        _ctx.putImageData(_imgdata, 0, 0)

        return Surface(surf=_canvas)

    def fill(self, color):
        """ fill canvas with this color """
        self.context.fillStyle = base.tuple_to_css_color(color)
        self.context.fillRect(0, 0, self._canvas.width, self._canvas.height)

    # -----------------
    #  properties
    # -----------------
    @property
    def canvas(self):
        return self._canvas

    @property
    def colorkey(self):
        return self._chosen_colorkey

    @property
    def context(self):
        return self._canvas.getContext('2d')

    @property
    def imagetype(self):
        return self._js_image is not None

    @property
    def jsimage(self):
        return self._js_image

    @property
    def height(self):
        return self._size[1]

    @property
    def width(self):
        return self._size[0]

    # -----------------
    #  getters (for a proper pygame mod. emulation)
    # -----------------
    def get_size(self):
        return self._size

    def get_height(self):
        return self._size[1]

    def get_width(self):
        return self._size[0]

    # def scroll(self, dx=0, dy=0):
    #     _imgdata = self._context.toDataURL('image/png')
    #     self._context.drawImage(_imgdata, dx, dy)
    #
    # def get_at(self, pos):
    #     # returns rgb
    #     return self._context.getImageData(pos[0], pos[1], 1, 1).data
    #
    # def set_at(self, pos, color):
    #     self._context.fillStyle = 'rgb(%s,%s,%s)' % color
    #     self._context.fillRect(pos[0], pos[1], 1, 1)

    def get_rect(self, centerx=None, centery=None):
        return Rect(0, 0, self._canvas.width, self._canvas.height)

    def set_colorkey(self, keycolor, flags=None):
        self._chosen_colorkey = keycolor[0:3]  # we wand an RGB value
