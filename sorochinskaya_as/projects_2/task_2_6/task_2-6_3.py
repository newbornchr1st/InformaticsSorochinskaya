donor_phenotype = input("Введите фенотип группы крови донора (I, II, III, IV): ").strip().upper()
recipient_phenotype = input("Введите фенотип группы крови реципиента (I, II, III, IV): ").strip().upper()


if donor_phenotype == "I" or donor_phenotype == recipient_phenotype or recipient_phenotype == "IV":
    print("Переливание возможно :)")
else:
    print("Переливание невозможно :(")