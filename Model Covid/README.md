Data yang digunakan merupakan dataset hasil tes COVID-19 yang diambil dari laman ministry of health

Data berisi kolom sebagai berikut:
    test_date: Arrival date of the test at the lab in DD/MM/YY format
    gender: test taker's sex: male/female/ NULL (unknown); appears from March 22nd 2020
    Corona_result: Results of first Covid-19 test, by category:
    a. Positive – carrying Covid-19
    b. Negative – not carrying Covid-19
    Age_60_and_above: Indicator of the test taker's age - 60 or over (1) or below 60 (0). Appears from March 17th 2020.
    cough: Did cough symptoms appear before testing? 1 – Yes, 0 – No, NULL – Unknown
    fever: Did fever appear before testing? 1 – Yes, 0 – No, NULL - Unknown
    Sore_throat: Did sore throat symptoms appear before testing? 1 – Yes, 0 – No, NULL - Unknown
    Shortness_of_breath: Did cough shortness of breath symptoms appear before testing? 1 – Yes, 0 – No, NULL- Unknown
    Head_ache: Did headache symptoms appear before testing? 1 – Yes, 0 – No, NULL - Unknown
    Test_indication: What is the indication for testing? Abroad – arrived from abroad,
    contact_with_confirmed – contact with a confirmed case, other – other indication or not specified

Model menggunakan DecisionTree sebagai model akhir terbaik.