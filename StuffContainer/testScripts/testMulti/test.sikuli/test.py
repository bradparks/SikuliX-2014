Debug.on(3)
s0 = Screen(0)
Debug.logp("0: %s", s0)
s1 = Screen(1)
Debug.logp("1: %s", s1)
"""
s0.hover()
wait(2)
s1.hover()
wait(2)
s0.hover()
"""
bsw = App("Safari").open().window()
bsw.highlight(1)
img = "img.png"
m = s1.find(img)
hover(m)
hover(s1)
saveCapture("test")
m = bsw.find("_test.png")
hover(m)

icons = "icons.png"
hover(icons)
