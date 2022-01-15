import pyglet
 
anim = pyglet.image.load_animation('hackhack/rubik.gif')
animSprite = pyglet.sprite.Sprite(anim)
 
w = animSprite.width
h = animSprite.height
 
window = pyglet.window.Window(width=w, height=h)
 
r,g,b,alpha = 0.5,0.5,0.8,0.5
 
pyglet.gl.glClearColor(r,g,b,alpha)
 
@window.event
def on_draw():
    window.clear()
    animSprite.draw()

pyglet.app.run()