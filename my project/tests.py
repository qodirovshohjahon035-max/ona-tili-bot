# tests.py

ALL_TESTS = [
    # 1–30 testlar
    {
        "question": "1. Qaysi qatorda faqat jarangsiz undoshlar berilgan?",
        "options": ["A) b, d, g", "B) p, t, k", "C) v, z, j", "D) m, n, l"],
        "correct_option": 1,
        "explanation": "To'g'ri javob: p, t, k."
    },
    {
        "question": "2. Qaysi so'zda harflar soni tovushlar sonidan ko'p?",
        "options": ["A) kitob", "B) tong", "C) bola", "D) olma"],
        "correct_option": 1,
        "explanation": "To'g'ri javob: tong (ng harflari bitta tovushni bildiradi)."
    },
    {
        "question": "3. Qaysi qatorda sinonim so'zlar berilgan?",
        "options": ["A) katta – kichik", "B) go'zal – chiroyli", "C) oq – qora", "D) kelmoq – ketmoq"],
        "correct_option": 1,
        "explanation": "To'g'ri javob: go'zal – chiroyli."
    },
    {
        "question": "4. Qaysi qatorda antonim (zid ma'noli) so'zlar berilgan?",
        "options": ["A) yaxshi – yomon", "B) tez – shiddatli", "C) uy – xona", "D) ota – dada"],
        "correct_option": 0,
        "explanation": "To'g'ri javob: yaxshi – yomon."
    },
    {
        "question": "5. Qaysi so'z omonim (shakldosh) bo'la oladi?",
        "options": ["A) kitob", "B) o'rik", "C) qo'y", "D) daftar"],
        "correct_option": 2,
        "explanation": "To'g'ri javob: qo'y (ot va fe'l ma'nolarida keladi)."
    },
    {
        "question": "6. \"Daftarimiz\" so'zidagi egalik qo'shimchasi qaysi shaxs va sonda?",
        "options": ["A) I shaxs, birlik", "B) I shaxs, ko'plik", "C) II shaxs, birlik", "D) III shaxs, ko'plik"],
        "correct_option": 1,
        "explanation": "To'g'ri javob: I shaxs, ko'plik (-imiz)."
    },
    {
        "question": "7. \"Maktabga bordim\" gapidagi \"maktabga\" so'zi qaysi kelishikda?",
        "options": ["A) Qaratqich", "B) Tushum", "C) Jo'nalish", "D) O'rin-payt"],
        "correct_option": 2,
        "explanation": "To'g'ri javob: Jo'nalish kelishigi."
    },
    {
        "question": "8. Qaysi so'zda qaratqich kelishigi qo'shimchasi qo'llangan?",
        "options": ["A) kitobni", "B) kitobning", "C) kitobga", "D) kitobda"],
        "correct_option": 1,
        "explanation": "To'g'ri javob: kitobning."
    },
    {
        "question": "9. \"Chiroyliroq\" so'zida sifatning qaysi darajasini yasovchi qo'shimcha bor?",
        "options": ["A) -roq (qiyosiy daraja)", "B) -gina (ozaytirma)", "C) -dor (otdan sifat yasovchi)", "D) -siz (inkor)"],
        "correct_option": 0,
        "explanation": "To'g'ri javob: -roq (qiyosiy daraja)."
    },
    {
        "question": "10. \"Beshinchi\" so'zi sonning qaysi turiga kiradi?",
        "options": ["A) Sanoq son", "B) Tartib son", "C) Dona son", "D) Taqsim son"],
        "correct_option": 1,
        "explanation": "To'g'ri javob: Tartib son."
    },
    {
        "question": "11. \"Kim?\" so'zi qaysi olmosh turiga kiradi?",
        "options": ["A) Kishilik olmoshi", "B) Ko'rsatish olmoshi", "C) So'roq olmoshi", "D) Belgilash olmoshi"],
        "correct_option": 2,
        "explanation": "To'g'ri javob: So'roq olmoshi."
    },
    {
        "question": "12. \"Yuvindi\" fe'li qaysi nisbatda?",
        "options": ["A) Aniq nisbat", "B) O'zlik nisbat", "C) Majhul nisbat", "D) Birgalik nisbat"],
        "correct_option": 1,
        "explanation": "To'g'ri javob: O'zlik nisbat."
    },
    {
        "question": "13. Qaysi fe'l majhul nisbat shaklida?",
        "options": ["A) yozdi", "B) yozdirdi", "C) yozildi", "D) yozishdi"],
        "correct_option": 2,
        "explanation": "To'g'ri javob: yozildi."
    },
    {
        "question": "14. Qaysi so'z to'g'ri yozilgan?",
        "options": ["A) masul", "B) mas'ul", "C) ma'sul", "D) masu'l"],
        "correct_option": 1,
        "explanation": "To'g'ri javob: mas'ul."
    },
    {
        "question": "15. Qaysi so'zda tutuq belgisi noto'g'ri qo'yilgan?",
        "options": ["A) ma'no", "B) san'at", "C) mu'jiza", "D) kita'b"],
        "correct_option": 3,
        "explanation": "To'g'ri javob: kita'b."
    },
    {
        "question": "16. Qaysi so'z takroriy so'z hisoblanadi?",
        "options": ["A) qo'l-oyoq", "B) tez-tez", "C) ko'z-qosh", "D) ota-ona"],
        "correct_option": 1,
        "explanation": "To'g'ri javob: tez-tez."
    },
    {
        "question": "17. O'zbek tilida nechta unli tovush bor?",
        "options": ["A) 5", "B) 6", "C) 9", "D) 10"],
        "correct_option": 1,
        "explanation": "To'g'ri javob: 6 ta."
    },
    {
        "question": "18. \"Qo'li ochiq\" iborasining ma'nosi qaysi?",
        "options": ["A) baxil", "B) saxiy", "C) dangasa", "D) kuchli"],
        "correct_option": 1,
        "explanation": "To'g'ri javob: saxiy."
    },
    {
        "question": "19. \"Asta gapirdi\" gapidagi \"asta\" so'zi qaysi turkumga kiradi?",
        "options": ["A) Sifat", "B) Ravish", "C) Olmosh", "D) Son"],
        "correct_option": 1,
        "explanation": "To'g'ri javob: Ravish."
    },
    {
        "question": "20. \"Ammo, biroq, lekin\" so'zlari qaysi bog'lovchilar guruhiga kiradi?",
        "options": ["A) Biriktiruv bog'lovchilari", "B) Ayiruv bog'lovchilari", "C) Zidlov bog'lovchilari", "D) Sabab bog'lovchilari"],
        "correct_option": 2,
        "explanation": "To'g'ri javob: Zidlov bog'lovchilari."
    },
    {
        "question": "21. Qaysi so'z yuklama?",
        "options": ["A) hatto", "B) va", "C) uchun", "D) bilan"],
        "correct_option": 0,
        "explanation": "To'g'ri javob: hatto."
    },
    {
        "question": "22. Qaysi so'z undov so'z?",
        "options": ["A) oh", "B) ammo", "C) hatto", "D) uchun"],
        "correct_option": 0,
        "explanation": "To'g'ri javob: oh."
    },
    {
        "question": "23. Ega va kesim ot bilan ifodalanganda, ular orasiga qaysi tinish belgisi qo'yiladi?",
        "options": ["A) Vergul", "B) Tire", "C) Nuqtali vergul", "D) Ikki nuqta"],
        "correct_option": 1,
        "explanation": "To'g'ri javob: Tire."
    },
    {
        "question": "24. \"Ali, kitobni ol.\" gapida undalma qaysi?",
        "options": ["A) Ali", "B) kitobni", "C) ol", "D) Undalma yo'q"],
        "correct_option": 0,
        "explanation": "To'g'ri javob: Ali."
    },
    {
        "question": "25. Gapda ega qaysi so'roqlarga javob bo'ladi?",
        "options": ["A) kim? nima?", "B) kimni? nimani?", "C) qanday? qaysi?", "D) qayerda? qachon?"],
        "correct_option": 0,
        "explanation": "To'g'ri javob: kim? nima?."
    },
    {
        "question": "26. Qaratqich aniqlovchi qaysi so'roqqa javob bo'ladi?",
        "options": ["A) qanday?", "B) kimning?", "C) nechta?", "D) qachon?"],
        "correct_option": 1,
        "explanation": "To'g'ri javob: kimning?."
    },
    {
        "question": "27. \"Yomg'ir yog'di, lekin biz sayrga chiqdik.\" gapi qaysi turga kiradi?",
        "options": ["A) Sodda gap", "B) Bog'langan qo'shma gap", "C) Ergash gapli qo'shma gap", "D) Bog'lovchisiz qo'shma gap"],
        "correct_option": 1,
        "explanation": "To'g'ri javob: Bog'langan qo'shma gap."
    },
    {
        "question": "28. \"Men uyda o'tirdim.\" gapida \"uyda\" so'zi qaysi gap bo'lagi?",
        "options": ["A) Ega", "B) To'ldiruvchi", "C) Hol", "D) Aniqlovchi"],
        "correct_option": 2,
        "explanation": "To'g'ri javob: Hol."
    },
    {
        "question": "29. \"Ular\" so'zi qaysi olmosh turiga kiradi?",
        "options": ["A) Kishilik olmoshi", "B) Ko'rsatish olmoshi", "C) So'roq olmoshi", "D) Belgilash olmoshi"],
        "correct_option": 0,
        "explanation": "To'g'ri javob: Kishilik olmoshi."
    },
    {
        "question": "30. Qaysi so'z sifatdosh?",
        "options": ["A) o'qib", "B) o'qigan", "C) o'qish", "D) o'qidi"],
        "correct_option": 1,
        "explanation": "To'g'ri javob: o'qigan."
    },

    # 31–60 testlar
    {
        "question": "31. Qaysi gapda ega va kesim orasiga tire qo'yiladi?",
        "options": ["A) Ali kitob o'qidi.", "B) Bolalar o'ynayapti.", "C) Toshkent – O'zbekistonning poytaxti.", "D) U uyga keldi."],
        "correct_option": 2,
        "explanation": "To'g'ri javob: Toshkent – O'zbekistonning poytaxti."
    },
    {
        "question": "32. Qaysi gapda payt ergash gap qatnashgan?",
        "options": ["A) Men bilamanki, u keladi.", "B) Agar yomg'ir yog'sa, biz chiqmaymiz.", "C) Qor yog'gani uchun yo'l yopildi.", "D) Bahor kelganda, daraxtlar gullaydi."],
        "correct_option": 3,
        "explanation": "To'g'ri javob: Bahor kelganda, daraxtlar gullaydi."
    },
    {
        "question": "33. Qaysi qatorda faqat yasama so'zlar berilgan?",
        "options": ["A) o'qituvchi, bilimdon, ishchi", "B) kitob, daftar, qalam", "C) uy, bog', ko'cha", "D) katta, kichik, uzun"],
        "correct_option": 0,
        "explanation": "To'g'ri javob: o'qituvchi, bilimdon, ishchi."
    },
    {
        "question": "34. Qaysi so'z o'zlashma qatlamga kiradi?",
        "options": ["A) qo'l", "B) kitob", "C) tosh", "D) ko'z"],
        "correct_option": 1,
        "explanation": "To'g'ri javob: kitob."
    },
    {
        "question": "35. \"Ko'z ochib yumguncha\" iborasining ma'nosi qaysi?",
        "options": ["A) juda sekin", "B) uxlab qolmoq", "C) juda tez, bir lahzada", "D) yig'lamoq"],
        "correct_option": 2,
        "explanation": "To'g'ri javob: juda tez, bir lahzada."
    },
    {
        "question": "36. Qaysi fe'l shart mayli shaklida?",
        "options": ["A) o'qisa", "B) o'qisin", "C) o'qigan", "D) o'qiydi"],
        "correct_option": 0,
        "explanation": "To'g'ri javob: o'qisa."
    },
    {
        "question": "37. \"Oq ko'ngil\" so'z birikmasida qaysi bog'lanish usuli qo'llangan?",
        "options": ["A) moslashuv", "B) boshqaruv", "C) qo'shma so'z", "D) bitishuv"],
        "correct_option": 3,
        "explanation": "To'g'ri javob: bitishuv."
    },
    {
        "question": "38. Qaysi birikmada boshqaruv usuli qo'llangan?",
        "options": ["A) kitobni o'qimoq", "B) yangi uy", "C) uyning eshigi", "D) tez yurmoq"],
        "correct_option": 0,
        "explanation": "To'g'ri javob: kitobni o'qimoq."
    },
    {
        "question": "39. Qaysi qatorda so'z bo'g'inlarga to'g'ri ajratilgan?",
        "options": ["A) kit-ob-lar", "B) kito-blar", "C) ki-tob-lar", "D) ki-to-blar"],
        "correct_option": 2,
        "explanation": "To'g'ri javob: ki-tob-lar."
    },
    {
        "question": "40. Qaysi so'z uch bo'g'inli?",
        "options": ["A) kitob", "B) bolalar", "C) daraxt", "D) maktab"],
        "correct_option": 1,
        "explanation": "To'g'ri javob: bolalar."
    },
    {
        "question": "41. Qaysi gapda so'z ko'chma ma'noda qo'llangan?",
        "options": ["A) Oltin uzuk taqdi.", "B) Temir eshik ochildi.", "C) Tosh uyni ko'rdim.", "D) U oltin qo'l usta."],
        "correct_option": 3,
        "explanation": "To'g'ri javob: U oltin qo'l usta."
    },
    {
        "question": "42. Qaysi gapda undalma bor?",
        "options": ["A) Do'stim keldi.", "B) Do'stim, menga yordam ber.", "C) Men do'stimni ko'rdim.", "D) Bu mening do'stim."],
        "correct_option": 1,
        "explanation": "To'g'ri javob: Do'stim, menga yordam ber."
    },
    {
        "question": "43. Qaysi qatorda sifatdosh qo'shimchalari berilgan?",
        "options": ["A) -ib, -gach", "B) -ish, -moq", "C) -gan, -ayotgan, -adigan", "D) -di, -sa"],
        "correct_option": 2,
        "explanation": "To'g'ri javob: -gan, -ayotgan, -adigan."
    },
    {
        "question": "44. Qaysi gapda ravishdosh qatnashgan?",
        "options": ["A) Kelgan odam ketdi.", "B) O'qish – yoshlik vazifasi.", "C) Men keldim.", "D) Ali kulib gapirdi."],
        "correct_option": 3,
        "explanation": "To'g'ri javob: Ali kulib gapirdi."
    },
    {
        "question": "45. Qaysi qatorda barcha so'zlar to'g'ri yozilgan?",
        "options": ["A) a'zo, mano, san'at", "B) azo, ma'no, san'at", "C) a'zo, ma'no, sanat", "D) a'zo, ma'no, san'at"],
        "correct_option": 3,
        "explanation": "To'g'ri javob: a'zo, ma'no, san'at."
    },
    {
        "question": "46. Qaysi so'z to'g'ri yozilgan?",
        "options": ["A) mashgulot", "B) mashg'ulod", "C) mashg'ulot", "D) mashxulot"],
        "correct_option": 2,
        "explanation": "To'g'ri javob: mashg'ulot."
    },
    {
        "question": "47. Qaysi gapda bosh harf noto'g'ri ishlatilgan?",
        "options": ["A) Mening Do'stim Alisher keldi.", "B) Navoiy ko'chasi shahar markazida joylashgan.", "C) Biz Samarqand shahriga bordik.", "D) Ular Amudaryo bo'yida dam olishdi."],
        "correct_option": 0,
        "explanation": "To'g'ri javob: Mening Do'stim Alisher keldi."
    },
    {
        "question": "48. Qaysi gapda ikki nuqta to'g'ri qo'llangan?",
        "options": ["A) Men: bozordan olma oldim.", "B) Men bozordan: olma, anor va uzum oldim.", "C) Men bozordan olma: oldim.", "D) Men bozordan olma oldim:."],
        "correct_option": 1,
        "explanation": "To'g'ri javob: Men bozordan: olma, anor va uzum oldim."
    },
    {
        "question": "49. Qaysi so'z ko'makchi?",
        "options": ["A) va", "B) ham", "C) hatto", "D) uchun"],
        "correct_option": 3,
        "explanation": "To'g'ri javob: uchun."
    },
    {
        "question": "50. Qaysi qatorda faqat ot yasovchi qo'shimchalar berilgan?",
        "options": ["A) -chi, -lik, -zor", "B) -li, -siz, -dor", "C) -la, -lash, -ay", "D) -gina, -roq, -mtir"],
        "correct_option": 0,
        "explanation": "To'g'ri javob: -chi, -lik, -zor."
    },
    {
        "question": "51. Qaysi gap bo'lagi ikkinchi darajali bo'lak emas?",
        "options": ["A) aniqlovchi", "B) to'ldiruvchi", "C) kesim", "D) hol"],
        "correct_option": 2,
        "explanation": "To'g'ri javob: kesim."
    },
    {
        "question": "52. \"Men sening kelishingni kutdim.\" gapida \"kelishingni\" qaysi gap bo'lagi?",
        "options": ["A) ega", "B) kesim", "C) hol", "D) to'ldiruvchi"],
        "correct_option": 3,
        "explanation": "To'g'ri javob: to'ldiruvchi."
    },
    {
        "question": "53. Qaysi qatorda bog'lovchisiz qo'shma gap berilgan?",
        "options": ["A) Yomg'ir yog'di va ko'chalar ho'l bo'ldi.", "B) Yomg'ir yog'di, ko'chalar ho'l bo'ldi.", "C) Yomg'ir yog'di, lekin ko'chalar quruq edi.", "D) Yomg'ir yog'gani uchun ko'chalar ho'l bo'ldi."],
        "correct_option": 1,
        "explanation": "To'g'ri javob: Yomg'ir yog'di, ko'chalar ho'l bo'ldi."
    },
    {
        "question": "54. \"Agar vaqt bo'lsa, men senga yordam beraman.\" gapida ergash gap qaysi turga kiradi?",
        "options": ["A) payt ergash gap", "B) sabab ergash gap", "C) shart ergash gap", "D) maqsad ergash gap"],
        "correct_option": 2,
        "explanation": "To'g'ri javob: shart ergash gap."
    },
    {
        "question": "55. Qaysi fe'l orttirma nisbatda?",
        "options": ["A) yuvdirdi", "B) yuvildi", "C) yuvindi", "D) yuvishdi"],
        "correct_option": 0,
        "explanation": "To'g'ri javob: yuvdirdi."
    },
    {
        "question": "56. Qaysi so'z sifatning orttirma darajasini bildiradi?",
        "options": ["A) oqroq", "B) oqish", "C) oq", "D) oppoq"],
        "correct_option": 3,
        "explanation": "To'g'ri javob: oppoq."
    },
    {
        "question": "57. Kelishiklar to'g'ri tartibda qaysi qatorda berilgan?",
        "options": [
            "A) bosh, tushum, qaratqich, jo'nalish, o'rin-payt, chiqish",
            "B) bosh, qaratqich, tushum, jo'nalish, o'rin-payt, chiqish",
            "C) bosh, jo'nalish, qaratqich, tushum, o'rin-payt, chiqish",
            "D) bosh, qaratqich, tushum, o'rin-payt, jo'nalish, chiqish"
        ],
        "correct_option": 1,
        "explanation": "To'g'ri javob: bosh, qaratqich, tushum, jo'nalish, o'rin-payt, chiqish."
    },
    {
        "question": "58. Qaysi so'z turkumi gap bo'lagi bo'la olmaydi?",
        "options": ["A) ot", "B) fe'l", "C) bog'lovchi", "D) sifat"],
        "correct_option": 2,
        "explanation": "To'g'ri javob: bog'lovchi."
    },
    {
        "question": "59. \"Qush uyasida ko'rganini qiladi\" maqolining ma'nosi qaysi?",
        "options": ["A) Bola oilada ko'rganiga amal qiladi.", "B) Qushlar uyada yashaydi.", "C) Uya qurish qiyin.", "D) Qushlar chiroyli bo'ladi."],
        "correct_option": 0,
        "explanation": "To'g'ri javob: Bola oilada ko'rganiga amal qiladi."
    },
    {
        "question": "60. Qaysi so'z to'g'ri yozilgan?",
        "options": ["A) o'qtuvchi", "B) o'qituvchi", "C) oqituvchi", "D) o'kituvchi"],
        "correct_option": 1,
        "explanation": "To'g'ri javob: o'qituvchi."
    },

    # 61–90 testlar
    {
        "question": "61. Qaysi so'z qo'shma so'z hisoblanadi?",
        "options": ["A) o'qituvchi", "B) oqqush", "C) bolalar", "D) yurmoq"],
        "correct_option": 1,
        "explanation": "To'g'ri javob: oqqush."
    },
    {
        "question": "62. Qaysi so'z juft so'z?",
        "options": ["A) ko'zoynak", "B) tez-tez", "C) kitob-daftar", "D) yashil"],
        "correct_option": 2,
        "explanation": "To'g'ri javob: kitob-daftar."
    },
    {
        "question": "63. Qaysi qatorda so'zlar o'zbek alifbosi tartibida joylashgan?",
        "options": [
            "A) o'rik, olma, pista, qovun",
            "B) qovun, pista, olma, o'rik",
            "C) olma, o'rik, pista, qovun",
            "D) olma, pista, qovun, o'rik"
        ],
        "correct_option": 3,
        "explanation": "To'g'ri javob: olma, pista, qovun, o'rik."
    },
    {
        "question": "64. Qaysi so'zda jarangli undosh talaffuzda jarangsizga o'tadi?",
        "options": ["A) bola", "B) ona", "C) kitob", "D) uy"],
        "correct_option": 2,
        "explanation": "To'g'ri javob: kitob."
    },
    {
        "question": "65. Qaysi qatorda faqat lablangan unlilar berilgan?",
        "options": ["A) a, e, i", "B) o, u, o'", "C) a, o, u", "D) i, e, o'"],
        "correct_option": 1,
        "explanation": "To'g'ri javob: o, u, o'."
    },
    {
        "question": "66. Qaysi so'z fors-tojik tilidan o'zlashgan?",
        "options": ["A) kitob", "B) qalam", "C) vaqt", "D) daraxt"],
        "correct_option": 3,
        "explanation": "To'g'ri javob: daraxt."
    },
    {
        "question": "67. \"Yer bilan yakson bo'lmoq\" iborasining ma'nosi qaysi?",
        "options": ["A) yiqilib tushmoq", "B) butunlay vayron bo'lmoq", "C) uxlab qolmoq", "D) yugurib ketmoq"],
        "correct_option": 1,
        "explanation": "To'g'ri javob: butunlay vayron bo'lmoq."
    },
    {
        "question": "68. \"Og'zi qulog'ida\" iborasining ma'nosi qaysi?",
        "options": ["A) g'azablangan", "B) charchagan", "C) juda xursand", "D) kasal"],
        "correct_option": 2,
        "explanation": "To'g'ri javob: juda xursand."
    },
    {
        "question": "69. \"Tilini tishlamoq\" iborasining ma'nosi qaysi?",
        "options": ["A) qattiq yig'lab yubormoq", "B) baland ovozda kulmoq", "C) ovqatni tez yemoq", "D) aytganidan afsuslanib jim qolmoq"],
        "correct_option": 3,
        "explanation": "To'g'ri javob: aytganidan afsuslanib jim qolmoq."
    },
    {
        "question": "70. \"Ko'p yashagan emas, ko'p ko'rgan biladi\" maqolining ma'nosi qaysi?",
        "options": ["A) Tajriba hayotda ko'proq narsa o'rgatadi.", "B) Katta yoshdagilar doim haq.", "C) Ko'p ko'rish zararli.", "D) Kam gapirish kerak."],
        "correct_option": 0,
        "explanation": "To'g'ri javob: Tajriba hayotda ko'proq narsa o'rgatadi."
    },
    {
        "question": "71. Qaysi gapda vositasiz to'ldiruvchi bor?",
        "options": ["A) Bahor keldi.", "B) Ali kitobni o'qidi.", "C) Biz uyda o'tirdik.", "D) Havo issiq."],
        "correct_option": 1,
        "explanation": "To'g'ri javob: Ali kitobni o'qidi."
    },
    {
        "question": "72. \"Biz ertaga sayohatga chiqamiz.\" gapida \"ertaga\" qaysi gap bo'lagi?",
        "options": ["A) payt holi", "B) o'rin holi", "C) sabab holi", "D) maqsad holi"],
        "correct_option": 0,
        "explanation": "To'g'ri javob: payt holi."
    },
    {
        "question": "73. \"U kasal bo'lgani uchun darsga kelmadi.\" gapidagi ergash gap turi qaysi?",
        "options": ["A) shart ergash gap", "B) payt ergash gap", "C) sabab ergash gap", "D) maqsad ergash gap"],
        "correct_option": 2,
        "explanation": "To'g'ri javob: sabab ergash gap."
    },
    {
        "question": "74. Qaysi gapda kirish so'z bor?",
        "options": ["A) Ali keldi.", "B) Aftidan, yomg'ir yog'adi.", "C) Biz uyga bordik.", "D) U kitob o'qidi."],
        "correct_option": 1,
        "explanation": "To'g'ri javob: Aftidan, yomg'ir yog'adi."
    },
    {
        "question": "75. Qaysi gapda vergul noto'g'ri qo'yilgan?",
        "options": ["A) Ali, Vali va Sobir keldi.", "B) Yomg'ir yog'di, lekin biz chiqdik.", "C) Men, bozorga bordim.", "D) Bahor kelganda, daraxtlar gulladi."],
        "correct_option": 2,
        "explanation": "To'g'ri javob: Men, bozorga bordim."
    },
    {
        "question": "76. Qaysi gapda undalma to'g'ri ajratilgan?",
        "options": ["A) Ota, bugun bozorga boraman.", "B) Ota bugun, bozorga boraman.", "C) Ota bugun bozorga, boraman.", "D) Ota bugun bozorga boraman,."],
        "correct_option": 0,
        "explanation": "To'g'ri javob: Ota, bugun bozorga boraman."
    },
    {
        "question": "77. \"Qani, tezroq yur!\" gapi maqsadga ko'ra qaysi turga kiradi?",
        "options": ["A) Darak gap", "B) So'roq gap", "C) Buyruq gap", "D) Ergash gap"],
        "correct_option": 2,
        "explanation": "To'g'ri javob: Buyruq gap."
    },
    {
        "question": "78. Qaysi gap yig'iq gap?",
        "options": ["A) Bahorda daraxtlar gulladi.", "B) Bahor keldi.", "C) Qizil gul ochildi.", "D) Biz bog'ga bordik."],
        "correct_option": 1,
        "explanation": "To'g'ri javob: Bahor keldi."
    },
    {
        "question": "79. Qaysi fe'l bo'lishsiz shaklda?",
        "options": ["A) o'qidi", "B) o'qiydi", "C) o'qisin", "D) o'qimadi"],
        "correct_option": 3,
        "explanation": "To'g'ri javob: o'qimadi."
    },
    {
        "question": "80. Qaysi fe'l o'tgan zamonda?",
        "options": ["A) o'qiyapti", "B) o'qidi", "C) o'qiydi", "D) o'qimoqchi"],
        "correct_option": 1,
        "explanation": "To'g'ri javob: o'qidi."
    },
    {
        "question": "81. Qaysi so'z taqsim son?",
        "options": ["A) uchta", "B) beshtadan", "C) ikkinchi", "D) o'nlab"],
        "correct_option": 1,
        "explanation": "To'g'ri javob: beshtadan."
    },
    {
        "question": "82. Qaysi so'z o'zlik olmoshi?",
        "options": ["A) biz", "B) bu", "C) kim", "D) o'z"],
        "correct_option": 3,
        "explanation": "To'g'ri javob: o'z."
    },
    {
        "question": "83. Qaysi so'z payt ravishi?",
        "options": ["A) hozir", "B) tez", "C) yaxshi", "D) juda"],
        "correct_option": 0,
        "explanation": "To'g'ri javob: hozir."
    },
    {
        "question": "84. Qaysi so'z to'g'ri yozilgan?",
        "options": ["A) masuliyat", "B) mas'uliyat", "C) masuliyyat", "D) masulyat"],
        "correct_option": 1,
        "explanation": "To'g'ri javob: mas'uliyat."
    },
    {
        "question": "85. Qaysi qatorda barcha so'zlar to'g'ri yozilgan?",
        "options": [
            "A) jamiyat, ijtimoiy, e'tibor",
            "B) jamiyat, ijtimoyi, e'tibor",
            "C) jam'iyat, ijtimoiy, e'tibor",
            "D) jamiyat, ijtimoiy, etibor"
        ],
        "correct_option": 0,
        "explanation": "To'g'ri javob: jamiyat, ijtimoiy, e'tibor."
    },
    {
        "question": "86. Qaysi so'zda bitta tovush ikki harf bilan yoziladi?",
        "options": ["A) olma", "B) kitob", "C) shahar", "D) ota"],
        "correct_option": 2,
        "explanation": "To'g'ri javob: shahar."
    },
    {
        "question": "87. Qaysi so'zda egalik qo'shimchasi noto'g'ri qo'shilgan?",
        "options": ["A) kitobim", "B) daftaring", "C) uysi", "D) qalami"],
        "correct_option": 2,
        "explanation": "To'g'ri javob: uysi."
    },
    {
        "question": "88. Qaysi so'zga egalik qo'shimchasi qo'shilganda unli tovush tushib qoladi?",
        "options": ["A) kitob", "B) o'rin", "C) bola", "D) daftar"],
        "correct_option": 1,
        "explanation": "To'g'ri javob: o'rin."
    },
    {
        "question": "89. Qaysi so'zga egalik qo'shimchasi qo'shilganda k tovushi g ga o'zgaradi?",
        "options": ["A) yurak", "B) kitob", "C) ko'cha", "D) bola"],
        "correct_option": 0,
        "explanation": "To'g'ri javob: yurak."
    },
    {
        "question": "90. Qaysi qatorda paronimlar (shakli yaqin, ma'nosi boshqa so'zlar) berilgan?",
        "options": ["A) katta – kichik", "B) go'zal – chiroyli", "C) ot – ot", "D) asl – asil"],
        "correct_option": 3,
        "explanation": "To'g'ri javob: asl – asil."
    },

    # 171–190 testlar
    {
        "question": "171. \"Quyosh kulib qaradi\" jumlasida qaysi badiiy san'at bor?",
        "options": ["A) o'xshatish", "B) mubolag'a", "C) sifatlash", "D) jonlantirish"],
        "correct_option": 3,
        "explanation": "To'g'ri javob: jonlantirish."
    },
    {
        "question": "172. \"Yuzi oydek yorug'\" jumlasida qaysi badiiy san'at bor?",
        "options": ["A) jonlantirish", "B) o'xshatish", "C) mubolag'a", "D) sifatlash"],
        "correct_option": 1,
        "explanation": "To'g'ri javob: o'xshatish."
    },
    {
        "question": "173. Qaysi gapda \"o'qigan\" so'zi otlashgan?",
        "options": ["A) O'qiganlar keldi.", "B) O'qigan bola keldi.", "C) U kitob o'qigan.", "D) Bola o'qigan."],
        "correct_option": 0,
        "explanation": "To'g'ri javob: O'qiganlar keldi."
    },
    {
        "question": "174. Qaysi gapda sifat otlashgan?",
        "options": ["A) Katta uy ko'rindi.", "B) Katta bolalar keldi.", "C) Kattalar yig'ildi.", "D) Katta shahar ko'rindi."],
        "correct_option": 2,
        "explanation": "To'g'ri javob: Kattalar yig'ildi."
    },
    {
        "question": "175. \"Bolalarimizning\" so'zida nechta qo'shimcha bor?",
        "options": ["A) 3", "B) 5", "C) 4", "D) 2"],
        "correct_option": 0,
        "explanation": "To'g'ri javob: 3."
    },
    {
        "question": "176. Qaysi so'z -chi qo'shimchasi bilan yasalgan?",
        "options": ["A) bola", "B) kitob", "C) maktab", "D) ishchi"],
        "correct_option": 3,
        "explanation": "To'g'ri javob: ishchi."
    },
    {
        "question": "177. So'zning ma'noli eng kichik bo'lagi nima?",
        "options": ["A) bo'g'in", "B) tovush", "C) morfema", "D) harf"],
        "correct_option": 2,
        "explanation": "To'g'ri javob: morfema."
    },
    {
        "question": "178. So'zning qo'shimchasiz, lug'aviy ma'no bildiruvchi asosiy qismi nima?",
        "options": ["A) o'zak", "B) qo'shimcha", "C) negiz", "D) affiks"],
        "correct_option": 0,
        "explanation": "To'g'ri javob: o'zak."
    },
    {
        "question": "179. \"Bolalik\" so'zining o'zagi qaysi?",
        "options": ["A) bolalik", "B) lik", "C) bola", "D) bo"],
        "correct_option": 2,
        "explanation": "To'g'ri javob: bola."
    },
    {
        "question": "180. \"Yangilik\" so'zi qaysi so'z turkumiga kiradi?",
        "options": ["A) sifat", "B) fe'l", "C) ravish", "D) ot"],
        "correct_option": 3,
        "explanation": "To'g'ri javob: ot."
    },
    {
        "question": "181. Qaysi qo'shimcha fe'ldan ot yasaydi?",
        "options": ["A) -lik", "B) -(u)v", "C) -dor", "D) -siz"],
        "correct_option": 1,
        "explanation": "To'g'ri javob: -(u)v."
    },
    {
        "question": "182. Qaysi qo'shimcha otdan sifat yasaydi?",
        "options": ["A) -li", "B) -uv", "C) -moq", "D) -ish"],
        "correct_option": 0,
        "explanation": "To'g'ri javob: -li."
    },
    {
        "question": "183. Qaysi qatorda faqat fe'l yasovchi qo'shimchalar berilgan?",
        "options": ["A) -chi, -lik, -zor", "B) -li, -siz, -dor", "C) -la, -lash, -lan", "D) -gina, -roq, -ish"],
        "correct_option": 2,
        "explanation": "To'g'ri javob: -la, -lash, -lan."
    },
    {
        "question": "184. Qaysi so'z juftligi omonim?",
        "options": ["A) tut (daraxt) – tut (fe'l)", "B) katta – kichik", "C) oq – qora", "D) yaxshi – yaxshiroq"],
        "correct_option": 0,
        "explanation": "To'g'ri javob: tut (daraxt) – tut (fe'l)."
    },
    {
        "question": "185. Qaysi so'z juftligi sinonim?",
        "options": ["A) ota – ona", "B) olim – bilimdon", "C) katta – kichik", "D) kelmoq – ketmoq"],
        "correct_option": 1,
        "explanation": "To'g'ri javob: olim – bilimdon."
    },
    {
        "question": "186. Qaysi gapda ikkinchi darajali bo'lak yo'q?",
        "options": ["A) Biz bog'da o'ynadik.", "B) Men yaxshi kitob o'qidim.", "C) U bugun keldi.", "D) Bolalar o'ynayapti."],
        "correct_option": 3,
        "explanation": "To'g'ri javob: Bolalar o'ynayapti."
    },
    {
        "question": "187. Qaysi so'z ko'rsatish olmoshi?",
        "options": ["A) men", "B) kim", "C) hamma", "D) bu"],
        "correct_option": 3,
        "explanation": "To'g'ri javob: bu."
    },
    {
        "question": "188. Qaysi so'z son turkumiga kiradi?",
        "options": ["A) bola", "B) tez", "C) o'nta", "D) uzun"],
        "correct_option": 2,
        "explanation": "To'g'ri javob: o'nta."
    },
    {
        "question": "189. \"Chunki\" bog'lovchisi qaysi ergash gapni bosh gapga bog'laydi?",
        "options": ["A) sabab", "B) payt", "C) maqsad", "D) shart"],
        "correct_option": 0,
        "explanation": "To'g'ri javob: sabab."
    },
    {
        "question": "190. \"Uchun\" so'zi qaysi so'z turkumiga kiradi?",
        "options": ["A) bog'lovchi", "B) ko'makchi", "C) yuklama", "D) undov"],
        "correct_option": 1,
        "explanation": "To'g'ri javob: ko'makchi."
    }
]
