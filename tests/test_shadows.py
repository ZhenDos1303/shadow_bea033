from shadow.polyedr import Polyedr
from common.tk_drawer import TkDrawer


class TestShadowCount:
    def setup_method(self):
        self.tk = TkDrawer()

    def test_shadow_count1(self):
        polyedr = Polyedr(f"data/cube_modified.geom")
        polyedr.draw(self.tk)
        assert polyedr.count_shadows() == 2.0

    def test_shadow_count2(self):
        polyedr = Polyedr(f"data/cube_modified2.geom")
        polyedr.draw(self.tk)
        assert polyedr.count_shadows() == 1.25
