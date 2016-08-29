import unittest
from string_manipulation import *

class TestStringManipulation(unittest.TestCase):

	def test_character_counts(self):

		result = character_counts("all of the things are different and yet all of the same")
		self.assertEqual(result, {'a': 5, ' ': 11, 'e': 7, 'd': 2, 'g': 1, 'f': 4, 'i': 2, 'h': 3, 'm': 1, 'l': 4, 'm': 1, 'n': 3, 'o': 2, 'r': 2, 's': 2, 't': 5, 'y':1})

		result = character_counts("this string will result in a different dictionary when passed into charachter counts")
		self.assertEqual(result, {'a': 5, ' ': 12, 'c': 4, 'e': 6, 'd': 3, 'g': 1, 'f': 2, 'i': 8, 'h': 4, 'l': 3, 'o': 3, 'n': 7, 'p': 1, 's': 6, 'r': 6, 'u': 2, 't': 8, 'w': 2, 'y': 1})

	def test_combine_strings(self):

		string_list = ["I think ", "that I will have a good time ", "writing code today ", "I will learn a lot"]

		result = combine_strings(string_list)
		self.assertEqual(result, "I think that I will have a good time writing code today I will learn a lot")

	def test_break_into_sentence(self):

		sample_text = "Lorem ipsum dolor sit amet, nam nostro delicata percipitur ea, nonumes constituto te sit, sed ex maiorum lobortis consulatu. In vivendum legendos vis, dolor contentiones pro no. In pri esse laboramus, ex constituto intellegam voluptatibus est, debitis mandamus sea ei. Usu vitae intellegam te, ea usu causae menandri. Te esse libris quo, iracundia dissentiunt cu sit, purto perpetua partiendo in usu. Te fierent consulatu sea, qui quaeque nominati assentior te. Cum ut feugait interesset, ne sed semper ocurreret. No sit putant percipit mediocritatem. Ius falli accusam ei. Ne vis persius fuisset. An explicari dissentiunt usu. Fierent erroribus assueverit mei id, ei utinam patrioque his. Iusto mundi scribentur quo an, an affert qualisque inciderint mea. Minimum eloquentiam cum an, hinc mentitum comprehensam pri eu. Nec exerci gubergren in, salutandi gloriatur usu an, habemus evertitur eu ius. Ne vel hendrerit elaboraret voluptatibus, ius oratio placerat ut. Paulo partem referrentur at vis, ut scaevola reprehendunt est. Duo cu nibh quas, usu id odio sententiae. Ea quem vidit solum mea. Sea case aeterno discere ut, tantas nominavi sea id, no per harum molestie. Ex novum affert mei. Everti bonorum nam id. Quo semper labitur quaestio at. Audire persecuti adolescens no mea, his semper omnium commodo an. Lorem facilisi ea vis. Commodo discere nec te, at sale persius neglegentur pri. Quem exerci complectitur quo cu. Malis principes molestiae te sit. Dolorum sadipscing v."

		result = break_into_sentence(sample_text)
		self.assertEqual(result, ['Lorem ipsum dolor sit amet, nam nostro delicata percipitur ea, nonumes constituto te sit, sed ex maiorum lobortis consulatu.', 'In vivendum legendos vis, dolor contentiones pro no.', 'In pri esse laboramus, ex constituto intellegam voluptatibus est, debitis mandamus sea ei.', 'Usu vitae intellegam te, ea usu causae menandri.', 'Te esse libris quo, iracundia dissentiunt cu sit, purto perpetua partiendo in usu.', 'Te fierent consulatu sea, qui quaeque nominati assentior te.', 'Cum ut feugait interesset, ne sed semper ocurreret.', 'No sit putant percipit mediocritatem.', 'Ius falli accusam ei.', 'Ne vis persius fuisset.', 'An explicari dissentiunt usu.', 'Fierent erroribus assueverit mei id, ei utinam patrioque his.', 'Iusto mundi scribentur quo an, an affert qualisque inciderint mea.', 'Minimum eloquentiam cum an, hinc mentitum comprehensam pri eu.', 'Nec exerci gubergren in, salutandi gloriatur usu an, habemus evertitur eu ius.', 'Ne vel hendrerit elaboraret voluptatibus, ius oratio placerat ut.', 'Paulo partem referrentur at vis, ut scaevola reprehendunt est.', 'Duo cu nibh quas, usu id odio sententiae.', 'Ea quem vidit solum mea.', 'Sea case aeterno discere ut, tantas nominavi sea id, no per harum molestie.', 'Ex novum affert mei.', 'Everti bonorum nam id.', 'Quo semper labitur quaestio at.', 'Audire persecuti adolescens no mea, his semper omnium commodo an.', 'Lorem facilisi ea vis.', 'Commodo discere nec te, at sale persius neglegentur pri.', 'Quem exerci complectitur quo cu.', 'Malis principes molestiae te sit.', 'Dolorum sadipscing v.'])

	def test_sentence_length(self):

		test_paragraph = "Lorem ipsum dolor sit amet, ut mutat primis impetus eam, hinc accusam ei eam, agam putent his ex. Platonem percipitur an qui, ut nam eripuit impedit iudicabit. Usu ex sapientem temporibus, vim ei graeci delectus. Deserunt inimicus pri ad, vero expetendis in his, quo quod verear ea.  Everti noluisse pri cu, pro ne melius erroribus. Paulo mucius has ut, eos et postea impedit. Admodum fabellas repudiare at eam, te dictas consequat mea. His ad everti melius, est et omnis melius docendi, mel facilis evertitur moderatius eu.  Eu porro molestiae democritum nam. Delenit repudiandae sea id, pro ea appetere lobortis recteque. Id nam quis graeco eloquentiam, eam magna sanctus splendide at, sea quando aperiam consulatu te. Sea ut graeco forensibus, qui duis ubique ut, dico cetero petentium at eum. Ea brute neglegentur eam, sit integre delicata interpretaris ei. Qui te option epicurei reprimique, solum assum affert mei at.  No vide electram complectitur cum, ex alii cibo etiam pro. Nobis semper postulant nam eu. Ius ne quod lorem eruditi. Te saepe verear facilis est. No vidit verear vel."

		result = count_length(test_paragraph)
		self.assertEqual(result, {'Ius ne quod lorem eruditi.': 26, 'Deserunt inimicus pri ad, vero expetendis in his, quo quod verear ea.': 69, 'Qui te option epicurei reprimique, solum assum affert mei at.': 61, 'Id nam quis graeco eloquentiam, eam magna sanctus splendide at, sea quando aperiam consulatu te.': 96, 'Platonem percipitur an qui, ut nam eripuit impedit iudicabit.': 61, 'His ad everti melius, est et omnis melius docendi, mel facilis evertitur moderatius eu.': 87, 'Nobis semper postulant nam eu.': 30, 'Sea ut graeco forensibus, qui duis ubique ut, dico cetero petentium at eum.': 75, 'No vidit verear vel.': 20, 'Delenit repudiandae sea id, pro ea appetere lobortis recteque.': 62, 'Ea brute neglegentur eam, sit integre delicata interpretaris ei.': 64, ' Everti noluisse pri cu, pro ne melius erroribus.': 49, 'Lorem ipsum dolor sit amet, ut mutat primis impetus eam, hinc accusam ei eam, agam putent his ex.': 97, 'Paulo mucius has ut, eos et postea impedit.': 43, ' Eu porro molestiae democritum nam.': 35, 'Usu ex sapientem temporibus, vim ei graeci delectus.': 52, 'Te saepe verear facilis est.': 28, 'Admodum fabellas repudiare at eam, te dictas consequat mea.': 59, ' No vide electram complectitur cum, ex alii cibo etiam pro.': 59})


if __name__ == '__main__':
	unittest.main()