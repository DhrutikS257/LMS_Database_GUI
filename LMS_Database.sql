
-- Question 5
-- SELECT bl.card_no,b.title, julianday(bl.returned_date) - julianday(bl.due_date) Late_Day
-- FROM BOOK_LOANS bl
-- NATURAL JOIN BOOK b
-- WHERE (bl.due_date BETWEEN '2022-02-01' AND '2022-02-06') And bl.Late = 1;


-- Question 6 a
-- -- for no parameters entered 
-- SELECT card_no,name, 
--     CASE WHEN LateFeeBalance > 0 THEN '$'||LateFeeBalance ELSE '$0.00' END
-- FROM vBookLoanInfo
-- ORDER BY LateFeeBalance DESC;

-- -- for borrower_id
-- SELECT card_no,name, 
--     CASE WHEN LateFeeBalance > 0 THEN '$'||LateFeeBalance ELSE '$0.00' END
-- FROM vBookLoanInfo
-- WHERE card_no = '{card_no}'
-- ORDER BY card_no DESC;

-- name
-- SELECT card_no,name, 
--     CASE WHEN LateFeeBalance > 0 THEN '$'||LateFeeBalance ELSE '$0.00' END
-- FROM vBookLoanInfo
-- WHERE name LIKE '%{name}%'
-- ORDER BY card_no DESC;


-- Question 6b

-- no filter
-- SELECT title, 
--     CASE WHEN LateFeeBalance > 0 THEN
--     (CASE When LateFeeBalance LIKE '%.__' THEN '$'||LateFeeBalance ELSE '$'||LateFeeBalance||'0' END)
--     ELSE 'N/A' END Late_Fee
-- FROM vBookLoanInfo
-- ORDER BY LateFeeBalance DESC;

-- book_id
-- SELECT title, 
--     CASE WHEN LateFeeBalance > 0 THEN
--     (CASE When LateFeeBalance LIKE '%.__' THEN '$'||LateFeeBalance ELSE '$'||LateFeeBalance||'0' END)
--     ELSE 'N/A' END Late_Fee
-- FROM vBookLoanInfo
-- NATURAL JOIN BOOK b
-- WHERE b.book_id = '{book_id}'
-- ORDER BY LateFeeBalance DESC;

-- book_title
-- SELECT title, 
--     CASE WHEN LateFeeBalance > 0 THEN
--     (CASE When LateFeeBalance LIKE '%.__' THEN '$'||LateFeeBalance ELSE '$'||LateFeeBalance||'0' END)
--     ELSE 'N/A' END Late_Fee
-- FROM vBookLoanInfo
-- WHERE title LIKE '%{book_title}%'
-- ORDER BY LateFeeBalance DESC;


















