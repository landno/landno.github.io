import os
from bs4 import BeautifulSoup
count=0
for i in os.listdir('xhtml'):
	print('count:'+str(722-count))
	count+=1
	soup = BeautifulSoup(open('xhtml/'+i).read(),'html.parser')
	#soup = BeautifulSoup(open('xhtml/3.xhtml').read(),'html.parser')
	h = soup.find('h1')
	meta = soup.find('meta',attrs={'property':'og:url'})
	#print(meta['content'][34:36])

	if h:
		t = h.text
		if t == '一、若想擁有，普施一切':
			os.system('cp xhtml/'+i+' x_html/chap-6-sect-5-sub-a.html')
		if t == '二、若想平安，就藉著教導它來學會它':
			os.system('cp xhtml/'+i+' x_html/chap-6-sect-5-sub-b.html')
		if t == '三、只為上主及其天國而儆醒':
			os.system('cp xhtml/'+i+' x_html/chap-6-sect-5-sub-c.html')
		if t == '1 正文導言':
			os.system('cp xhtml/'+i+' x_html/text-intro.html')
		if t == '4 導言':
			os.system('cp xhtml/'+i+' x_html/chap-4-intro.html')
		if t == '5 導言':
			os.system('cp xhtml/'+i+' x_html/chap-5-intro.html')
		if t == '6 導言':
			os.system('cp xhtml/'+i+' x_html/chap-6-intro.html')
		if t == '10 導言':
			os.system('cp xhtml/'+i+' x_html/chap-10-intro.html')
		if t == '11 導言':
			os.system('cp xhtml/'+i+' x_html/chap-11-intro.html')
		if t == '13 導言':
			os.system('cp xhtml/'+i+' x_html/chap-13-intro.html')
		if t == '14 導言':
			os.system('cp xhtml/'+i+' x_html/chap-14-intro.html')
		if t == '21 導言':
			os.system('cp xhtml/'+i+' x_html/chap-21-intro.html')
		if t == '22 導言':
			os.system('cp xhtml/'+i+' x_html/chap-22-intro.html')
		if t == '23 導言':
			os.system('cp xhtml/'+i+' x_html/chap-23-intro.html')
		if t == '24 導言':
			os.system('cp xhtml/'+i+' x_html/chap-24-intro.html')
		if t == '25 導言':
			os.system('cp xhtml/'+i+' x_html/chap-25-intro.html')
		if t == '30 導言':
			os.system('cp xhtml/'+i+' x_html/chap-30-intro.html')
			#break
		if len(t.split(' ')) == 2 and meta['content'][34:36] == '1.':
			if len(t.split(' ')[0].split('-')) == 2:
				fn = 'chap-'+t.split(' ')[0].split('-')[0]+'-sect-'+t.split(' ')[0].split('-')[1]+'.html'
				os.system('cp xhtml/'+i+' x_html/'+fn)

		#workbook
		if meta['content'][34:36] == '2.':
			if h:
				t = h.text

				#error!!!!!!!!!!!!!!
				if t == '1 導言' and meta['content'][92:93] == '1':
					os.system('cp xhtml/'+i+' x_html/wb-intro.html')
				if t == '1 導言' and meta['content'][92:93] == '2':
					os.system('cp xhtml/'+i+' x_html/wb-part2-intro.html')
				if t == '51～60課 複習一：導言':
					os.system('cp xhtml/'+i+' x_html/review-1-intro.html')
				if t == '81～90課 複習二：導言':
					os.system('cp xhtml/'+i+' x_html/review-2-intro.html')
				if t == '111～120課 複習三：導言':
					os.system('cp xhtml/'+i+' x_html/review-3-intro.html')
				if t == '141～150課 複習四：導言':
					os.system('cp xhtml/'+i+' x_html/review-4-intro.html')
				if t == '171～180課 複習五：導言':
					os.system('cp xhtml/'+i+' x_html/review-5-intro.html')
				if t == '181～200課：導言':
					os.system('cp xhtml/'+i+' x_html/l-181-to-200-intro.html')
				if t == '201～220課 複習六：導言':
					os.system('cp xhtml/'+i+' x_html/review-6-intro.html')
				if t == '1. 何謂寬恕？':
					os.system('cp xhtml/'+i+' x_html/wb-part2-what-is-1.html')
				if t == '2. 何謂救恩？':
					os.system('cp xhtml/'+i+' x_html/wb-part2-what-is-2.html')
				if t == '3. 何謂世界？':
					os.system('cp xhtml/'+i+' x_html/wb-part2-what-is-3.html')
				if t == '4. 何謂罪？':
					os.system('cp xhtml/'+i+' x_html/wb-part2-what-is-4.html')
				if t == '5. 何謂身體？':
					os.system('cp xhtml/'+i+' x_html/wb-part2-what-is-5.html')
				if t == '6. 何謂基督？':
					os.system('cp xhtml/'+i+' x_html/wb-part2-what-is-6.html')
				if t == '7. 何謂聖靈？':
					os.system('cp xhtml/'+i+' x_html/wb-part2-what-is-7.html')
				if t == '8. 何謂真實世界？':
					os.system('cp xhtml/'+i+' x_html/wb-part2-what-is-8.html')
				if t == '9. 何謂基督的再臨？':
					os.system('cp xhtml/'+i+' x_html/wb-part2-what-is-9.html')
				if t == '10. 何謂最後的審判？':
					os.system('cp xhtml/'+i+' x_html/wb-part2-what-is-10.html')
				if t == '11. 何謂受造？':
					os.system('cp xhtml/'+i+' x_html/wb-part2-what-is-11.html')
				if t == '12. 何謂小我？':
					os.system('cp xhtml/'+i+' x_html/wb-part2-what-is-12.html')
				if t == '13. 何謂奇蹟？':
					os.system('cp xhtml/'+i+' x_html/wb-part2-what-is-13.html')
				if t == '14. 我是什麼？':
					os.system('cp xhtml/'+i+' x_html/wb-part2-what-is-14.html')
				if t == '361～365課 最後的幾課':
					os.system('cp xhtml/'+i+' x_html/final-lessons-intro.html')
				if t == '361～365課 最後的幾課':
					os.system('cp xhtml/'+i+' x_html/final-lessons.html')
				if t == '跋':
					os.system('cp xhtml/'+i+' x_html/wb-epilogue.html')
				if t.find('課') and len(t.split('課')[0])<4:
					os.system('cp xhtml/'+i+' x_html/lesson-'+t.split('課')[0]+'.html')

			pass
		#manual
		if meta['content'][34:36] == '3.':
			if h:
				t = h.text
				if t == '1 導言':
					os.system('cp xhtml/'+i+' x_html/manual-intro.html')
				if t.find('.')>1:
					os.system('cp xhtml/'+i+' x_html/manual-'+t.split('.')[0]+'.html')


		#p
		if meta['content'][34:36] == '4.':
			if h:
				t = h.text
				if t == '導言':
					os.system('cp xhtml/'+i+' x_html/clarification-intro.html')
				if t == '跋':
					os.system('cp xhtml/'+i+' x_html/clarification-epilogue.html')
				if t.find('.')>=1:
					os.system('cp xhtml/'+i+' x_html/clarification-0'+t.split('.')[0]+'.html')
		#s
		if meta['content'][34:36] == '5.':
			if t == '導言':
				os.system('cp xhtml/'+i+' x_html/psycho-intro.html')
			if t == '1 心理治療的目的':
				os.system('cp xhtml/'+i+' x_html/psycho-1.html')
			if t == '2 心理治療的過程——導言':
				os.system('cp xhtml/'+i+' x_html/psycho-2-intro.html')
			if t == '2-1 心理治療的限制':
				os.system('cp xhtml/'+i+' x_html/psycho-2-sect-1.html')
			if t == '2-2 宗教在心理治療中的位置':
				os.system('cp xhtml/'+i+' x_html/psycho-2-sect-2.html')
			if t == '2-3 心理治療師的角色':
				os.system('cp xhtml/'+i+' x_html/psycho-2-sect-3.html')
			if t == '2-4 罹病的過程':
				os.system('cp xhtml/'+i+' x_html/psycho-2-sect-4.html')
			if t == '2-5 療癒的過程':
				os.system('cp xhtml/'+i+' x_html/psycho-2-sect-5.html')
			if t == '2-6 療癒的定義':
				os.system('cp xhtml/'+i+' x_html/psycho-2-sect-6.html')
			if t == '2-7 理想的醫病關係':
				os.system('cp xhtml/'+i+' x_html/psycho-2-sect-7.html')
			if t == '3 心理治療的實踐；3-1 怎麼挑選病患':
				os.system('cp xhtml/'+i+' x_html/psycho-3-sect-1.html')
			if t == '3-2 心理治療是一項專業嗎？':
				os.system('cp xhtml/'+i+' x_html/psycho-3-sect-2.html')
			if t == '3-3 付費的問題':
				os.system('cp xhtml/'+i+' x_html/psycho-3-sect-3.html')
			if t == '1 祈禱——導言':
				os.system('cp xhtml/'+i+' x_html/song-1-intro.html')
			if t == '1-1 真正的祈禱':
				os.system('cp xhtml/'+i+' x_html/song-1-sect-1.html')
			if t == '1-2 祈禱的階梯':
				os.system('cp xhtml/'+i+' x_html/song-1-sect-2.html')
			if t == '1-3 為他人祈禱':
				os.system('cp xhtml/'+i+' x_html/song-1-sect-3.html')
			if t == '1-4 與他人一同祈禱':
				os.system('cp xhtml/'+i+' x_html/song-1-sect-4.html')
			if t == '1-5 階梯的盡頭':
				os.system('cp xhtml/'+i+' x_html/song-1-sect-5.html')
			if t == '2 寬恕——導言':
				os.system('cp xhtml/'+i+' x_html/song-2-intro.html')
			if t == '2-1 自我寬恕':
				os.system('cp xhtml/'+i+' x_html/song-2-sect-1.html')
			if t == '2-2 毀滅式的寬恕':
				os.system('cp xhtml/'+i+' x_html/song-2-sect-2.html')
			if t == '2-3 救恩性的寬恕':
				os.system('cp xhtml/'+i+' x_html/song-2-sect-3.html')
			if t == '3 療癒——導言':
				os.system('cp xhtml/'+i+' x_html/song-3-intro.html')
			if t == '3-1 疾病的起因':
				os.system('cp xhtml/'+i+' x_html/song-3-sect-1.html')
			if t == '3-2 真假療癒':
				os.system('cp xhtml/'+i+' x_html/song-3-sect-2.html')
			if t == '3-3 分裂與合一':
				os.system('cp xhtml/'+i+' x_html/song-3-sect-3.html')
			if t == '3-4 療癒的神聖性':
				os.system('cp xhtml/'+i+' x_html/song-3-sect-4.html')


