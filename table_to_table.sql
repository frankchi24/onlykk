UPDATE common_words_chinese
SET
      meaning1 = (SELECT meaning.field3 
                            FROM meaning
                            WHERE meaning.field1 = common_words_chinese.stem )
    , meaning2 = (SELECT meaning.field4
                            FROM meaning
                            WHERE meaning.field1 = common_words_chinese.stem )
	, meaning3 = (SELECT meaning.field5
                            FROM meaning
                            WHERE meaning.field1 = common_words_chinese.stem )
	, meaning4 = (SELECT meaning.field6
                            FROM meaning
                            WHERE meaning.field1 = common_words_chinese.stem )

WHERE
    EXISTS (
        SELECT *
        FROM meaning
        WHERE meaning.field1 = common_words_chinese.stem
    )