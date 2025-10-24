# FruitJamUTA
Universal Translator Assistant for the Fruit Jam

The files should be put in apps/UTA, with the .lng files all put in a subdirectory **langs**.


Enter text without punctuation, and UTA will match English words with the Alien languages. This is not true 
translation, but provides vocabulary you can use to translate into the target language. It will also match Alien words back 
to English. Because more than one English word may map to an Alien word, the back translation may look odd.

```
      _   _ _____  _
     | | | |_   _|/ \
     | | | | | | / _ \
     | |_| | | |/ ___ \
      \___/  |_/_/   \_\
      Universal        _...
      Translator     ,'    `.
      Assistant     /        \
                    |    -._  |
                    \    \  `._
                     \    \    `...
                      `-..-`.      `-._
                            `.      _,--
                             `.   -'
                              '. |
                               '.|
                                '
loading tlhingan
text: hello what is your name
 nuqneH nuq ghaH lIj pong
text: *lang vulcan
loading vulcan
text: live long and prosper
 tich tor ang tesmur
text: *help
      _   _ _____  _
     | | | |_   _|/ \
     | | | | | | / _ \
     | |_| | | |/ ___ \
      \___/  |_/_/   \_\
      Universal Translator Assistant
   Help commands:
   *help - this file
   *pItlh - quit program
   *lang [filename] - loads langs/filename.lng

    Languages: vulcan, tlhingan, mandoa, romulan
text: tich tor ang tesmur
 live long and prosper
text: *lang mandoa
loading mandoa
text: I love you
 ni riduurok gar
text: ni riduurok gar
 me love your
text: 
```
