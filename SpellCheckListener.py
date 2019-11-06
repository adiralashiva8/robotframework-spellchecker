from textblob import TextBlob
from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn

class SpellCheckListener:

    ROBOT_LISTENER_API_VERSION = 3

    def __init__(self):
        self.PRE_RUNNER = 0
        self.spell_check_file = open("SpellCheckResult.html","w")
        
        content = """
            <table border="1" style="width:100%; text-align: center;">
                <tr>
                    <th>Suite</th>
                    <th>Test</th>
                    <th>Actual Word</th>
                    <th>Suggested Word</th>
                    <th>Confidence</th>
                </tr>
        """
        self.spell_check_file.write(content.strip())

    def start_suite(self, data, result):
        # get all tests in suite
        self.test_count = len(data.tests)

        # Fetch words to be ignored
        if self.PRE_RUNNER == 0:
            self.IGNORE_WORDS = BuiltIn().get_variable_value("${IGNORE_WORDS}")
            self.PRE_RUNNER = 1

        # get suite name
        self.suite_name = data.name

    def end_test(self, data, test):
        if self.test_count != 0:

            # fetch page content using selenium library
            seleniumlib = BuiltIn().get_library_instance('SeleniumLibrary')
            text = seleniumlib.get_text("//body")

            # create textBlob object
            blob = TextBlob(str(text))

            # split text into words and iterate for each word
            for word in blob.words:

                # perform spell check, result contains (correct-text, confidence)
                spell = word.spellcheck()

                # compare actual word with corrected word
                # verifying the confidence of corrected, consider if it is 1.0 or above only
                if word != spell[0][0] and spell[0][1] >= 1.0:

                    # ignore corrected word if word with in IGNORE_WORDS
                    if word not in self.IGNORE_WORDS:

                        # log info to spell checker report
                        content = """
                            <tr>
                                <td>%s</td>
                                <td>%s</td>
                                <td>%s</td>
                                <td>%s</td>
                                <td>%s</td>
                            </tr>
                        """%(str(self.suite_name), str(test), str(word), str(spell[0][0]), str(spell[0][1]))
                        self.spell_check_file.write(content.strip())

    def close(self):
        # close spell check file on complete
        self.spell_check_file.write("</table>")
        self.spell_check_file.close()