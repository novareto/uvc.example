.. :doctest:
=======
Doctest
=======

uvc.example

:Test-Layer: functional

   >>> 1 + 1
   2

   >>> 4 * 4
   16

   >>> layer.create_application('app')

   >>> browser = layer.new_browser('http://localhost/app') 
   >>> browser.contents
