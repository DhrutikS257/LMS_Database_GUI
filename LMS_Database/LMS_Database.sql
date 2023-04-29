-- CREATE VIEW vBookLoanInfo 
-- AS SELECT b.card_no,b.name,bl.date_out,bl.due_date,bl.returned_date, julianday(bl.returned_date) - julianday(bl.date_out) TotalDays,bo.title,
--         CASE WHEN julianday(bl.returned_date) - julianday(bl.due_date) >= 0 THEN julianday(bl.returned_date) - julianday(bl.due_date) ELSE 0 END lateReturn,
--         lb.branch_id,
--         CASE WHEN julianday(bl.returned_date) - julianday(bl.due_date) >= 0 THEN ((julianday(bl.returned_date) - julianday(bl.due_date))*lb.LateFee) ELSE 0 END LateFeeBalance
-- FROM BORROWER b
-- JOIN BOOK_LOANS bl ON b.card_no = bl.card_no
-- JOIN BOOK bo ON bl.book_id = bo.book_id
-- JOIN LIBRARY_BRANCH lb ON bl.branch_id = lb.branch_id
-- GROUP BY bo.title;

SELECT * FROM vBookLoanInfo;