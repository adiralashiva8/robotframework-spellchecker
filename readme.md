# SpellChecker - Robotframework (selenium)

Listener to perform spell check in navigated web page using TextBlob, Robotframework (selenium) [![HitCount](http://hits.dwyl.io/adiralashiva8/robotframework-spellchecker.svg)](http://hits.dwyl.io/adiralashiva8/robotframework-spellchecker)

---

## How it works

 - Robotframework (selenium) will fetch current page content (in listener)
   ```
   seleniumlib = BuiltIn().get_library_instance('SeleniumLibrary')
   text = seleniumlib.get_text("//body")
   ```

 - Fetched page text is passed to [TextBlob](https://github.com/sloria/textblob)
   ```
   blob = TextBlob("Page Content here")
   ```

 - Split text into words and perform spell check for each word
   ```
   for word in blob.words:
      spell = word.spellcheck()
   ```

---

## Required Libraries

 - TextBlob
    ```
    pip install -U textblob
    python -m textblob.download_corpora
    ```

 - Robotframework
   ```
   pip install robotframework
   ```

 - Robotframework-selenium
   ```
   pip install robotframework-seleniumlibrary
   ```

---

## Steps to Use

 - Step 1: Download or clone this repo
   ```
   https://github.com/adiralashiva8/robotframework-spellchecker.git
   ```
 
 - Step 2: Copy `SpellCheckListener.py` to your project

 - Step 3: Execute test case/suites using SpellCheckListener
   ```
   robot --listener SpellCheckListener.py -V data.py test.robot
   ``` 

   > Note: Here data.py is variable file which contains words (list type), which need to be ignored while performing spell check

 - Step 4: `SpellCheckResult.html` will be generated after completion of suite

---

## Screenshot

<img src="/Report_Image.jpg" alt="Report_Image">

----

## Future Plan

 - Check for grammar
 - Provide better report

---

## Reference

 - [TextBlob](https://github.com/sloria/textblob)
 - [Robotframework Listener](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#listener-interface)
 - [Robotframework Selenium](https://github.com/robotframework/SeleniumLibrary)

---

## Limitations

 - Plural words
   > `errors` is considered as spelling mistake

 - Case sensitive
   > `Page` is considered as spelling mistake

 - Word endings with extra content not considered as error
   > `keyboardd` is not an error

 - Special chars in words
   > `don't` is considered as spelling mistake

---

*Special Thanks To:* 

*Idea by:*

 - [Hanumanth Rao Koritala]()

---

 :star: repo if you like it

---