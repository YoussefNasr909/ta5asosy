# 70 High-Quality SQL Practice Questions
sql_questions = [
    {
        "id": "sql-gen-01",
        "topic": "SQL",
        "subtopic": "Joins",
        "question": "What is the logical difference between `UNION` and `UNION ALL` when combining query results in SQL?",
        "options": [
            {"id": "A", "text": "UNION automatically removes duplicate rows from the combined result set, whereas UNION ALL retains all duplicate rows and executes faster"},
            {"id": "B", "text": "UNION ALL only works on numeric data types"},
            {"id": "C", "text": "UNION combines columns horizontally, while UNION ALL combines rows vertically"},
            {"id": "D", "text": "UNION ALL removes NULL values while UNION preserves them"}
        ],
        "correctAnswer": "A",
        "explanation": "UNION performs an implicit distinct/sort operation to eliminate duplicate tuples across both result sets. UNION ALL simply concatenates the record sets without deduplication, providing better performance.",
        "difficulty": "easy",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "sql-gen-02",
        "topic": "SQL",
        "subtopic": "GROUP BY & Aggregation",
        "question": "In what chronological order does the relational SQL query engine logically evaluate the following clauses?\n1. SELECT  2. FROM  3. WHERE  4. GROUP BY  5. HAVING  6. ORDER BY",
        "options": [
            {"id": "A", "text": "FROM -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY"},
            {"id": "B", "text": "SELECT -> FROM -> WHERE -> GROUP BY -> HAVING -> ORDER BY"},
            {"id": "C", "text": "FROM -> GROUP BY -> WHERE -> HAVING -> SELECT -> ORDER BY"},
            {"id": "D", "text": "WHERE -> FROM -> GROUP BY -> SELECT -> HAVING -> ORDER BY"}
        ],
        "correctAnswer": "A",
        "explanation": "Logical SQL query processing evaluates: 1) FROM (and JOINs), 2) WHERE (row filtering), 3) GROUP BY (aggregation), 4) HAVING (group filtering), 5) SELECT (projection & expressions), 6) ORDER BY (sorting).",
        "difficulty": "hard",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "sql-gen-03",
        "topic": "SQL",
        "subtopic": "NULL Values & Logic",
        "question": "What is the result of the SQL boolean expression: `SELECT (NULL = NULL);`?",
        "options": [
            {"id": "A", "text": "UNKNOWN (evaluated as NULL/falsy in boolean predicates)"},
            {"id": "B", "text": "TRUE (1)"},
            {"id": "C", "text": "FALSE (0)"},
            {"id": "D", "text": "Syntax Error"}
        ],
        "correctAnswer": "A",
        "explanation": "Under SQL three-valued logic (3VL), comparing anything to NULL with standard comparison operators (=, !=, <, >) yields UNKNOWN. To check for nullity, one must use `IS NULL`.",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "sql-gen-04",
        "topic": "SQL",
        "subtopic": "Aggregate Functions",
        "question": "A table `Employees` has 5 rows with salaries: 1000, 2000, NULL, 3000, and NULL. What will `SELECT AVG(salary), COUNT(salary), COUNT(*) FROM Employees;` return?",
        "options": [
            {"id": "A", "text": "AVG = 2000, COUNT(salary) = 3, COUNT(*) = 5"},
            {"id": "B", "text": "AVG = 1200, COUNT(salary) = 5, COUNT(*) = 5"},
            {"id": "C", "text": "AVG = 2000, COUNT(salary) = 5, COUNT(*) = 5"},
            {"id": "D", "text": "AVG = NULL, COUNT(salary) = 3, COUNT(*) = 3"}
        ],
        "correctAnswer": "A",
        "explanation": "Aggregate functions (except COUNT(*)) ignore NULLs. AVG calculates (1000 + 2000 + 3000) / 3 = 2000. COUNT(salary) counts non-nulls (3). COUNT(*) counts all table rows (5).",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "sql-gen-05",
        "topic": "SQL",
        "subtopic": "Subqueries",
        "question": "What is a 'Correlated Subquery' in SQL?",
        "options": [
            {"id": "A", "text": "A subquery that references one or more columns from the outer query, causing it to be evaluated once for each candidate row processed by the outer query"},
            {"id": "B", "text": "A subquery that returns a single scalar value and executes only once"},
            {"id": "C", "text": "A subquery used strictly inside the FROM clause as an inline view"},
            {"id": "D", "text": "A subquery that contains a UNION ALL statement"}
        ],
        "correctAnswer": "A",
        "explanation": "A correlated subquery depends on values from the outer query row. Because its execution relies on outer query values, it conceptually evaluates row-by-row.",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "sql-gen-06",
        "topic": "SQL",
        "subtopic": "Subqueries",
        "question": "How does `EXISTS` differ from `IN` when evaluating subqueries containing NULL values in the result set?",
        "options": [
            {"id": "A", "text": "`EXISTS` tests whether the subquery returns at least one row (even if the row contains NULL), whereas `NOT IN` fails completely (returns no rows) if the subquery returns any NULL value"},
            {"id": "B", "text": "`EXISTS` is only supported in MySQL"},
            {"id": "C", "text": "`IN` never evaluates NULLs while `EXISTS` converts them to 0"},
            {"id": "D", "text": "There is no difference in behavior"}
        ],
        "correctAnswer": "A",
        "explanation": "If a subquery contains even one NULL, `x NOT IN (subquery)` evaluates to UNKNOWN for all rows, returning an empty set. `NOT EXISTS` checks for row existence boolean flag and safely handles NULL values.",
        "difficulty": "hard",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "sql-gen-07",
        "topic": "SQL",
        "subtopic": "Window Functions",
        "question": "What is the difference between `RANK()` and `DENSE_RANK()` window functions when duplicate ranking values occur?",
        "options": [
            {"id": "A", "text": "`RANK()` leaves gaps in the ranking sequence following ties (e.g., 1, 2, 2, 4), while `DENSE_RANK()` assigns consecutive ranks without gaps (e.g., 1, 2, 2, 3)"},
            {"id": "B", "text": "`DENSE_RANK()` only ranks string columns"},
            {"id": "C", "text": "`RANK()` assigns unique random numbers to ties"},
            {"id": "D", "text": "`DENSE_RANK()` requires a GROUP BY clause"}
        ],
        "correctAnswer": "A",
        "explanation": "`RANK()` computes peer ties and skips subsequent ranking positions by the number of duplicates. `DENSE_RANK()` increments rank strictly by 1 for the next distinct rank group without gaps.",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "sql-gen-08",
        "topic": "SQL",
        "subtopic": "Window Functions",
        "question": "Which window function allows a query to access a column value from the preceding row within the same partition without writing a self-join?",
        "options": [
            {"id": "A", "text": "LAG()"},
            {"id": "B", "text": "LEAD()"},
            {"id": "C", "text": "FIRST_VALUE()"},
            {"id": "D", "text": "ROW_NUMBER()"}
        ],
        "correctAnswer": "A",
        "explanation": "`LAG(column, offset)` accesses data from a previous row at a specified physical offset prior to the current row within the partition. `LEAD()` accesses subsequent rows.",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "sql-gen-09",
        "topic": "SQL",
        "subtopic": "Common Table Expressions (CTEs)",
        "question": "Which SQL clause defines a Common Table Expression (CTE)?",
        "options": [
            {"id": "A", "text": "WITH"},
            {"id": "B", "text": "AS"},
            {"id": "C", "text": "CREATE VIEW TEMPORARY"},
            {"id": "D", "text": "DECLARE TABLE"}
        ],
        "correctAnswer": "A",
        "explanation": "A Common Table Expression (CTE) is defined using the `WITH cte_name AS (SELECT ...)` syntax, creating a named temporary result set available within the execution scope of that query.",
        "difficulty": "easy",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "sql-gen-10",
        "topic": "SQL",
        "subtopic": "Data Definition (DDL)",
        "question": "How does `TRUNCATE TABLE` differ from `DELETE FROM table_name;` without a WHERE clause?",
        "options": [
            {"id": "A", "text": "TRUNCATE is a DDL operation that deallocates data pages quickly, resets identity/auto-increment seeds, and logs minimal redo data, whereas DELETE is a DML statement that logs every individual row deletion"},
            {"id": "B", "text": "TRUNCATE deletes the table schema from the database"},
            {"id": "C", "text": "DELETE cannot be rolled back inside a transaction"},
            {"id": "D", "text": "TRUNCATE fires row-level DELETE triggers for each row"}
        ],
        "correctAnswer": "A",
        "explanation": "TRUNCATE TABLE drops data at the page allocation level rather than logging individual row deletions. It resets identity counters and does not fire individual row-level triggers.",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "sql-gen-11",
        "topic": "SQL",
        "subtopic": "Joins",
        "question": "What is the result of a `CROSS JOIN` between table A (4 rows) and table B (3 rows)?",
        "options": [
            {"id": "A", "text": "Cartesian product returning 12 rows (4 * 3)"},
            {"id": "B", "text": "An inner join returning 0 rows"},
            {"id": "C", "text": "A union returning 7 rows"},
            {"id": "D", "text": "A syntax error unless an ON clause is supplied"}
        ],
        "correctAnswer": "A",
        "explanation": "A CROSS JOIN produces the Cartesian product of the two tables, pairing every row of table A with every row of table B without any join predicate, returning 4 * 3 = 12 rows.",
        "difficulty": "easy",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "sql-gen-12",
        "topic": "SQL",
        "subtopic": "Joins",
        "question": "What is a 'Self-Join' in SQL and how must it be written?",
        "options": [
            {"id": "A", "text": "Joining a table to itself; requires using distinct table aliases (e.g. `FROM Employees e1 JOIN Employees e2 ON e1.manager_id = e2.emp_id`)"},
            {"id": "B", "text": "A join that automatically duplicates every row in the table"},
            {"id": "C", "text": "A join between a table and an in-memory temporary table"},
            {"id": "D", "text": "A join that does not require an ON condition"}
        ],
        "correctAnswer": "A",
        "explanation": "A self-join combines rows from the same table when hierarchical or relational references exist within it (e.g., employee to manager). Table aliases are mandatory to disambiguate column references.",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "sql-gen-13",
        "topic": "SQL",
        "subtopic": "Joins",
        "question": "Which join returns all rows when there is a match in either left or right table, filling with NULLs where matches do not exist?",
        "options": [
            {"id": "A", "text": "FULL OUTER JOIN"},
            {"id": "B", "text": "INNER JOIN"},
            {"id": "C", "text": "LEFT JOIN"},
            {"id": "D", "text": "NATURAL JOIN"}
        ],
        "correctAnswer": "A",
        "explanation": "FULL OUTER JOIN combines the results of both LEFT and RIGHT outer joins, returning all matching and non-matching rows from both participating tables.",
        "difficulty": "easy",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "sql-gen-14",
        "topic": "SQL",
        "subtopic": "Conditional Expressions",
        "question": "What will the following SQL statement output?\n`SELECT CASE WHEN 10 > 20 THEN 'A' WHEN 5 = 5 THEN 'B' ELSE 'C' END;`",
        "options": [
            {"id": "A", "text": "'B'"},
            {"id": "B", "text": "'A'"},
            {"id": "C", "text": "'C'"},
            {"id": "D", "text": "NULL"}
        ],
        "correctAnswer": "A",
        "explanation": "A CASE expression evaluates sequentially from top to bottom and returns the result of the first WHEN clause that evaluates to TRUE. 10 > 20 is false; 5 = 5 is true, returning 'B'.",
        "difficulty": "easy",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "sql-gen-15",
        "topic": "SQL",
        "subtopic": "NULL Values & Logic",
        "question": "What is the return value of `COALESCE(NULL, NULL, 'First non-null', 'Second non-null')` in standard SQL?",
        "options": [
            {"id": "A", "text": "'First non-null'"},
            {"id": "B", "text": "'Second non-null'"},
            {"id": "C", "text": "NULL"},
            {"id": "D", "text": "An array of all strings"}
        ],
        "correctAnswer": "A",
        "explanation": "The COALESCE() function evaluates its arguments in order and returns the first non-NULL expression among its parameters.",
        "difficulty": "easy",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "sql-gen-16",
        "topic": "SQL",
        "subtopic": "NULL Values & Logic",
        "question": "What does the function `NULLIF(val1, val2)` return when `val1 = val2`?",
        "options": [
            {"id": "A", "text": "NULL"},
            {"id": "B", "text": "val1"},
            {"id": "C", "text": "TRUE"},
            {"id": "D", "text": "0"}
        ],
        "correctAnswer": "A",
        "explanation": "NULLIF(a, b) returns NULL if both arguments are equal (a = b); otherwise it returns the first argument a. It is often used to prevent divide-by-zero errors (e.g. `col1 / NULLIF(col2, 0)`).",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "sql-gen-17",
        "topic": "SQL",
        "subtopic": "Filtering & WHERE Clause",
        "question": "Which SQL query correctly finds all customers whose last name starts with 'S' and is at least 4 characters long?",
        "options": [
            {"id": "A", "text": "WHERE last_name LIKE 'S___%'"},
            {"id": "B", "text": "WHERE last_name LIKE 'S*%'"},
            {"id": "C", "text": "WHERE last_name LIKE 'S__%'"},
            {"id": "D", "text": "WHERE last_name LIKE 'S%' AND LENGTH(last_name) < 4"}
        ],
        "correctAnswer": "A",
        "explanation": "'S' matches the first character, followed by three underscores '___' requiring at least three additional characters (total >= 4), followed by '%' matching zero or more subsequent characters.",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "sql-gen-18",
        "topic": "SQL",
        "subtopic": "GROUP BY & Aggregation",
        "question": "Why is the following query invalid in standard ANSI SQL?\n`SELECT department_id, MAX(salary), employee_name FROM Employees GROUP BY department_id;`",
        "options": [
            {"id": "A", "text": "Column `employee_name` is neither aggregated nor included in the GROUP BY clause"},
            {"id": "B", "text": "MAX() cannot be used alongside GROUP BY"},
            {"id": "C", "text": "The WHERE clause is missing"},
            {"id": "D", "text": "A query can only select one column when grouping"}
        ],
        "correctAnswer": "A",
        "explanation": "In standard SQL, any non-aggregated column appearing in the SELECT list must be explicitly listed in the GROUP BY clause, because each group must represent a single consolidated value.",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "sql-gen-19",
        "topic": "SQL",
        "subtopic": "GROUP BY & Aggregation",
        "question": "What is the primary difference between filtering with a `WHERE` clause versus a `HAVING` clause?",
        "options": [
            {"id": "A", "text": "`WHERE` filters individual rows before grouping and cannot contain aggregate functions; `HAVING` filters aggregated groups after GROUP BY and can contain aggregate functions"},
            {"id": "B", "text": "`HAVING` can only be used on string columns"},
            {"id": "C", "text": "`WHERE` is executed after SELECT, while `HAVING` is executed before FROM"},
            {"id": "D", "text": "`HAVING` replaces the need for an ON join clause"}
        ],
        "correctAnswer": "A",
        "explanation": "`WHERE` filters input rows prior to aggregation. `HAVING` filters group rows produced by GROUP BY, allowing conditions on aggregates like `HAVING COUNT(*) > 5`.",
        "difficulty": "easy",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "sql-gen-20",
        "topic": "SQL",
        "subtopic": "Pagination & Limiting",
        "question": "In modern ANSI SQL (SQL:2008 and PostgreSQL), which standard clause is used for pagination (skipping the first 20 rows and fetching the next 10 rows)?",
        "options": [
            {"id": "A", "text": "OFFSET 20 ROWS FETCH NEXT 10 ROWS ONLY;"},
            {"id": "B", "text": "LIMIT 20, 10;"},
            {"id": "C", "text": "SKIP 20 TAKE 10;"},
            {"id": "D", "text": "PAGE 2 SIZE 10;"}
        ],
        "correctAnswer": "A",
        "explanation": "The SQL:2008 standard standardizes pagination using the `OFFSET n ROWS FETCH NEXT m ROWS ONLY` syntax.",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "sql-gen-21",
        "topic": "SQL",
        "subtopic": "Subqueries",
        "question": "What does the query `SELECT * FROM Products WHERE price > ALL (SELECT price FROM Products WHERE category = 'Books');` accomplish?",
        "options": [
            {"id": "A", "text": "Returns products whose price is greater than the maximum price of any book"},
            {"id": "B", "text": "Returns products whose price is greater than the average book price"},
            {"id": "C", "text": "Returns products whose price is greater than at least one book"},
            {"id": "D", "text": "Returns all books ordered by price"}
        ],
        "correctAnswer": "A",
        "explanation": "The `> ALL` condition requires that the outer price must exceed every value returned by the subquery, meaning it must be strictly greater than the maximum book price.",
        "difficulty": "hard",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "sql-gen-22",
        "topic": "SQL",
        "subtopic": "Subqueries",
        "question": "What does the query `SELECT * FROM Products WHERE price > ANY (SELECT price FROM Products WHERE category = 'Books');` return?",
        "options": [
            {"id": "A", "text": "Returns products whose price is greater than the minimum price among all books"},
            {"id": "B", "text": "Returns products whose price is greater than all books"},
            {"id": "C", "text": "Returns only products with NULL prices"},
            {"id": "D", "text": "Returns products whose price matches the book median"}
        ],
        "correctAnswer": "A",
        "explanation": "`> ANY` evaluates to TRUE if the price is greater than at least one value returned by the subquery, which is logically equivalent to `price > MIN(price)` of that subquery.",
        "difficulty": "hard",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "sql-gen-23",
        "topic": "SQL",
        "subtopic": "Keys & Constraints",
        "question": "What is the difference between a `PRIMARY KEY` constraint and a `UNIQUE` constraint?",
        "options": [
            {"id": "A", "text": "A table can have only one PRIMARY KEY and it strictly disallows NULLs, whereas a table can have multiple UNIQUE constraints and columns with UNIQUE constraints may permit NULL values"},
            {"id": "B", "text": "UNIQUE constraints automatically create foreign keys"},
            {"id": "C", "text": "PRIMARY KEY can only be applied to integer columns"},
            {"id": "D", "text": "UNIQUE constraints cannot be indexed"}
        ],
        "correctAnswer": "A",
        "explanation": "A relation can have at most one PRIMARY KEY which forbids NULLs under Entity Integrity. Multiple UNIQUE constraints can exist per table, allowing NULLs in standard SQL.",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "sql-gen-24",
        "topic": "SQL",
        "subtopic": "Keys & Constraints",
        "question": "Which constraint ensures that numeric values in a column meet a specific condition (e.g. `salary > 0`) upon insertion or update?",
        "options": [
            {"id": "A", "text": "CHECK constraint"},
            {"id": "B", "text": "DEFAULT constraint"},
            {"id": "C", "text": "FOREIGN KEY constraint"},
            {"id": "D", "text": "IDENTITY constraint"}
        ],
        "correctAnswer": "A",
        "explanation": "A CHECK constraint specifies a boolean condition that all inserted and modified rows must satisfy, rejecting any change where the expression evaluates to FALSE.",
        "difficulty": "easy",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "sql-gen-25",
        "topic": "SQL",
        "subtopic": "Transactions & TCL",
        "question": "What is the SQL command to reverse all changes made during the current uncommitted transaction?",
        "options": [
            {"id": "A", "text": "ROLLBACK;"},
            {"id": "B", "text": "UNDO;"},
            {"id": "C", "text": "REVERT;"},
            {"id": "D", "text": "CANCEL TRANSACTION;"}
        ],
        "correctAnswer": "A",
        "explanation": "`ROLLBACK;` cancels the current transaction and reverts all modifications made by DML statements back to the state at transaction start (or to a specified savepoint).",
        "difficulty": "easy",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "sql-gen-26",
        "topic": "SQL",
        "subtopic": "Data Control (DCL)",
        "question": "Which pair of SQL commands belongs to Data Control Language (DCL) and manages database security permissions?",
        "options": [
            {"id": "A", "text": "GRANT and REVOKE"},
            {"id": "B", "text": "COMMIT and ROLLBACK"},
            {"id": "C", "text": "CREATE and DROP"},
            {"id": "D", "text": "INSERT and DELETE"}
        ],
        "correctAnswer": "A",
        "explanation": "DCL consists of GRANT (giving users specific permissions such as SELECT or INSERT on database objects) and REVOKE (withdrawing granted permissions).",
        "difficulty": "easy",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "sql-gen-27",
        "topic": "SQL",
        "subtopic": "Indexing & Query Performance",
        "question": "What does the `EXPLAIN` (or `EXPLAIN ANALYZE`) statement do when prepended to a SQL query?",
        "options": [
            {"id": "A", "text": "Displays the execution plan selected by the query optimizer, detailing table scans, index lookups, join algorithms, and estimated/actual costs"},
            {"id": "B", "text": "Provides an English language explanation of what the query returns"},
            {"id": "C", "text": "Automatically fixes syntax errors in the query"},
            {"id": "D", "text": "Encodes the query into binary machine code"}
        ],
        "correctAnswer": "A",
        "explanation": "`EXPLAIN` displays the query execution plan (Index Scan, Seq Scan, Nested Loop, Hash Join, etc.), helping developers identify bottlenecks and optimize performance.",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "sql-gen-28",
        "topic": "SQL",
        "subtopic": "String & Date Functions",
        "question": "What does standard ANSI SQL `CONCAT('Hello', ' ', 'World')` or the string concatenation operator `||` return?",
        "options": [
            {"id": "A", "text": "'Hello World'"},
            {"id": "B", "text": "NULL"},
            {"id": "C", "text": "An error"},
            {"id": "D", "text": "'HelloWorld'"}
        ],
        "correctAnswer": "A",
        "explanation": "`CONCAT()` and the standard SQL `||` operator concatenate multiple text strings sequentially into a single composite string.",
        "difficulty": "easy",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "sql-gen-29",
        "topic": "SQL",
        "subtopic": "Window Functions",
        "question": "What will `ROW_NUMBER() OVER (PARTITION BY department_id ORDER BY salary DESC)` compute for each row?",
        "options": [
            {"id": "A", "text": "A sequential integer (1, 2, 3...) starting over at 1 for each department, ranked from highest to lowest salary"},
            {"id": "B", "text": "The total number of employees in the department"},
            {"id": "C", "text": "The department average salary"},
            {"id": "D", "text": "A running sum of salaries"}
        ],
        "correctAnswer": "A",
        "explanation": "PARTITION BY resets the row numbering for each distinct `department_id`, and ORDER BY sorts rows within that partition so the top earner in each department receives row number 1.",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "sql-gen-30",
        "topic": "SQL",
        "subtopic": "Window Functions",
        "question": "Which window clause specifies an aggregation frame extending from the start of the partition to the current row for calculating a cumulative running total?",
        "options": [
            {"id": "A", "text": "ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW"},
            {"id": "B", "text": "ROWS BETWEEN CURRENT ROW AND UNBOUNDED FOLLOWING"},
            {"id": "C", "text": "RANGE BETWEEN 1 PRECEDING AND 1 FOLLOWING"},
            {"id": "D", "text": "PARTITION ALL ROWS"}
        ],
        "correctAnswer": "A",
        "explanation": "The window frame `ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW` includes every row from partition beginning up to the current row, calculating running sums.",
        "difficulty": "hard",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "sql-gen-31",
        "topic": "SQL",
        "subtopic": "Data Manipulation (DML)",
        "question": "What occurs if an `UPDATE` statement is executed without a `WHERE` clause?",
        "options": [
            {"id": "A", "text": "Every single row in the table is updated with the specified new values"},
            {"id": "B", "text": "Only the first row in the table is updated"},
            {"id": "C", "text": "The database aborts with a syntax error"},
            {"id": "D", "text": "No rows are updated"}
        ],
        "correctAnswer": "A",
        "explanation": "Without a WHERE clause, an UPDATE statement applies its SET assignments across every row in the table, which can accidentally overwrite entire datasets.",
        "difficulty": "easy",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "sql-gen-32",
        "topic": "SQL",
        "subtopic": "Data Manipulation (DML)",
        "question": "What is the result of executing `DELETE FROM Customers;`?",
        "options": [
            {"id": "A", "text": "All rows from Customers are deleted, but the table schema and column definitions remain intact"},
            {"id": "B", "text": "The Customers table is completely dropped from the database schema"},
            {"id": "C", "text": "Only rows containing NULLs are deleted"},
            {"id": "D", "text": "A syntax error occurs because WHERE is required"}
        ],
        "correctAnswer": "A",
        "explanation": "DELETE removes all rows from the table one-by-one while keeping the table structure, constraints, and indexes intact. DROP TABLE would remove structure and data.",
        "difficulty": "easy",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "sql-gen-33",
        "topic": "SQL",
        "subtopic": "Joins",
        "question": "Given two tables: `A` with values {1, 2, 2} and `B` with values {2, 2, 3}. How many rows are returned by `SELECT A.val FROM A INNER JOIN B ON A.val = B.val;`?",
        "options": [
            {"id": "A", "text": "4 rows"},
            {"id": "B", "text": "2 rows"},
            {"id": "C", "text": "1 row"},
            {"id": "D", "text": "5 rows"}
        ],
        "correctAnswer": "A",
        "explanation": "Value 2 appears twice in table A and twice in table B. Each match from A combines with every match in B, producing 2 * 2 = 4 rows.",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "sql-gen-34",
        "topic": "SQL",
        "subtopic": "Joins",
        "question": "Which SQL construct can be used to simulate a `FULL OUTER JOIN` in database systems that do not natively support it (such as older MySQL versions)?",
        "options": [
            {"id": "A", "text": "A LEFT JOIN combined with a RIGHT JOIN using UNION"},
            {"id": "B", "text": "An INNER JOIN combined with CROSS JOIN"},
            {"id": "C", "text": "A NATURAL JOIN followed by INTERSECT"},
            {"id": "D", "text": "A correlated subquery inside GROUP BY"}
        ],
        "correctAnswer": "A",
        "explanation": "`SELECT ... LEFT JOIN ... UNION SELECT ... RIGHT JOIN ...` returns all matching rows and non-matching rows from both sides, exactly emulating FULL OUTER JOIN.",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "sql-gen-35",
        "topic": "SQL",
        "subtopic": "Common Table Expressions (CTEs)",
        "question": "What is a 'Recursive CTE' primarily used for in SQL?",
        "options": [
            {"id": "A", "text": "Querying hierarchical or tree-structured data such as organizational charts, file system directories, and bill of materials"},
            {"id": "B", "text": "Encrypting stored procedures"},
            {"id": "C", "text": "Backing up table definitions across servers"},
            {"id": "D", "text": "Rebuilding indexes automatically"}
        ],
        "correctAnswer": "A",
        "explanation": "Recursive CTEs contain an anchor member UNION ALLed with a recursive member referencing the CTE itself, making them ideal for navigating parent-child hierarchies of arbitrary depth.",
        "difficulty": "hard",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "sql-gen-36",
        "topic": "SQL",
        "subtopic": "Pattern Matching & LIKE",
        "question": "If you need to search for a literal percent sign '%' in a text column using LIKE, how is this accomplished?",
        "options": [
            {"id": "A", "text": "Using an ESCAPE character, e.g.: `WHERE discount LIKE '%\\%%' ESCAPE '\\'`"},
            {"id": "B", "text": "By doubling the percent sign: `WHERE discount LIKE '%%%%'`"},
            {"id": "C", "text": "Using quotes: `WHERE discount LIKE '%\"%\"%'`"},
            {"id": "D", "text": "Literal percent searches are impossible with LIKE"}
        ],
        "correctAnswer": "A",
        "explanation": "The ESCAPE keyword defines an escape character (like '\\') that tells the pattern matching engine to treat the following '%' or '_' as a literal character rather than a wildcard.",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "sql-gen-37",
        "topic": "SQL",
        "subtopic": "Indexing & Query Performance",
        "question": "Why does wrapping an indexed column inside a scalar function in the WHERE clause (e.g. `WHERE UPPER(last_name) = 'SMITH'`) often cause a full table scan?",
        "options": [
            {"id": "A", "text": "Standard B-Tree indexes store raw column values; applying a function prevents the optimizer from doing a direct index seek unless a function-based (expression) index exists"},
            {"id": "B", "text": "UPPER() automatically converts tables into temporary views"},
            {"id": "C", "text": "B-Tree indexes cannot index uppercase characters"},
            {"id": "D", "text": "Functions in WHERE clauses are syntax errors"}
        ],
        "correctAnswer": "A",
        "explanation": "Because the index key is `last_name`, evaluating `UPPER(last_name)` makes the predicate non-sargable (Search Argument Able), forcing the engine to calculate UPPER() on every row via a full scan.",
        "difficulty": "hard",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "sql-gen-38",
        "topic": "SQL",
        "subtopic": "Indexing & Query Performance",
        "question": "What is an 'Index Covering Query' (Covering Index)?",
        "options": [
            {"id": "A", "text": "A query whose requested SELECT columns, join predicates, and WHERE filters are all contained within the index itself, avoiding any disk lookup to the base table"},
            {"id": "B", "text": "An index that covers all tables in the database schema"},
            {"id": "C", "text": "An index created exclusively on primary keys"},
            {"id": "D", "text": "A query that deletes unused indexes"}
        ],
        "correctAnswer": "A",
        "explanation": "A covering index contains all attributes requested by the query. The database engine executes an index-only scan without reading base table pages from disk (Index-Only Scan).",
        "difficulty": "hard",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "sql-gen-39",
        "topic": "SQL",
        "subtopic": "Subqueries",
        "question": "What type of subquery returns exactly one row and one column?",
        "options": [
            {"id": "A", "text": "Scalar Subquery"},
            {"id": "B", "text": "Table-Valued Subquery"},
            {"id": "C", "text": "Multi-Column Subquery"},
            {"id": "D", "text": "Correlated Multi-Row Subquery"}
        ],
        "correctAnswer": "A",
        "explanation": "A scalar subquery evaluates to a single atomic value (one row, one column) and can be used in expressions, SELECT projections, and comparison operators.",
        "difficulty": "easy",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "sql-gen-40",
        "topic": "SQL",
        "subtopic": "Sorting & ORDER BY",
        "question": "How are NULL values sorted in standard ANSI SQL when executing `ORDER BY column_name ASC`?",
        "options": [
            {"id": "A", "text": "Standard SQL leaves this implementation-defined, but allows `NULLS FIRST` or `NULLS LAST` to explicitly specify placement"},
            {"id": "B", "text": "NULLs are always converted to the number zero"},
            {"id": "C", "text": "NULLs are always excluded from the result set"},
            {"id": "D", "text": "NULLs trigger an immediate error"}
        ],
        "correctAnswer": "A",
        "explanation": "The ANSI standard provides `ORDER BY col ASC NULLS FIRST` or `NULLS LAST`. In PostgreSQL/Oracle, ASC defaults to NULLS LAST; in MySQL/SQL Server, NULLs are treated as the lowest values.",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "sql-gen-41",
        "topic": "SQL",
        "subtopic": "Set Operations",
        "question": "Which SQL set operator returns only the rows that exist in the first query result but NOT in the second query result?",
        "options": [
            {"id": "A", "text": "EXCEPT (or MINUS in Oracle)"},
            {"id": "B", "text": "INTERSECT"},
            {"id": "C", "text": "UNION ALL"},
            {"id": "D", "text": "CROSS APPLY"}
        ],
        "correctAnswer": "A",
        "explanation": "The standard SQL `EXCEPT` operator (called `MINUS` in Oracle) computes set difference: records in Query 1 that do not appear in Query 2.",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "sql-gen-42",
        "topic": "SQL",
        "subtopic": "Set Operations",
        "question": "Which SQL set operator returns only the common rows that appear in BOTH query results?",
        "options": [
            {"id": "A", "text": "INTERSECT"},
            {"id": "B", "text": "UNION"},
            {"id": "C", "text": "EXCEPT"},
            {"id": "D", "text": "OUTER JOIN"}
        ],
        "correctAnswer": "A",
        "explanation": "`INTERSECT` returns distinct rows that are output by both the first and second queries.",
        "difficulty": "easy",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "sql-gen-43",
        "topic": "SQL",
        "subtopic": "Data Definition (DDL)",
        "question": "Which SQL statement adds a foreign key constraint named `fk_orders_customer` to an existing table `Orders`?",
        "options": [
            {"id": "A", "text": "ALTER TABLE Orders ADD CONSTRAINT fk_orders_customer FOREIGN KEY (customer_id) REFERENCES Customers(id);"},
            {"id": "B", "text": "UPDATE Orders SET FOREIGN KEY (customer_id) = Customers(id);"},
            {"id": "C", "text": "CREATE FOREIGN KEY fk_orders_customer ON Orders(customer_id);"},
            {"id": "D", "text": "INSERT INTO Orders CONSTRAINT fk_orders_customer REFERENCES Customers(id);"}
        ],
        "correctAnswer": "A",
        "explanation": "Modifying existing tables to enforce foreign keys uses `ALTER TABLE <table> ADD CONSTRAINT <name> FOREIGN KEY (<col>) REFERENCES <parent_table>(<parent_col>)`.",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "sql-gen-44",
        "topic": "SQL",
        "subtopic": "Basic Queries & SELECT",
        "question": "What is the result of `SELECT 5 + NULL;` in standard SQL?",
        "options": [
            {"id": "A", "text": "NULL"},
            {"id": "B", "text": "5"},
            {"id": "C", "text": "0"},
            {"id": "D", "text": "An error"}
        ],
        "correctAnswer": "A",
        "explanation": "Any arithmetic operation (+, -, *, /) involving NULL yields NULL because an operation on an unknown quantity results in an unknown quantity.",
        "difficulty": "easy",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "sql-gen-45",
        "topic": "SQL",
        "subtopic": "Aggregate Functions",
        "question": "What is the output of `SELECT COUNT(1)` versus `SELECT COUNT(*)` on an existing table?",
        "options": [
            {"id": "A", "text": "They produce the exact same result: both count all rows in the table without filtering"},
            {"id": "B", "text": "COUNT(1) only counts the first column, while COUNT(*) counts all"},
            {"id": "C", "text": "COUNT(1) counts only rows where the primary key is 1"},
            {"id": "D", "text": "COUNT(*) fails if any row has a NULL"}
        ],
        "correctAnswer": "A",
        "explanation": "Modern SQL optimizers treat `COUNT(1)` and `COUNT(*)` identically; both evaluate to the total number of rows matching the query regardless of NULL values.",
        "difficulty": "easy",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "sql-gen-46",
        "topic": "SQL",
        "subtopic": "String & Date Functions",
        "question": "In standard SQL, which function extracts the year from a date column `order_date`?",
        "options": [
            {"id": "A", "text": "EXTRACT(YEAR FROM order_date)"},
            {"id": "B", "text": "GETYEAR(order_date)"},
            {"id": "C", "text": "YEAR_ONLY(order_date)"},
            {"id": "D", "text": "PARSE(order_date, 'Y')"}
        ],
        "correctAnswer": "A",
        "explanation": "The standard SQL syntax is `EXTRACT(part FROM date_expression)`, e.g., `EXTRACT(YEAR FROM order_date)`.",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "sql-gen-47",
        "topic": "SQL",
        "subtopic": "Views",
        "question": "When is an SQL View generally updatable (able to support direct INSERT, UPDATE, and DELETE statements)?",
        "options": [
            {"id": "A", "text": "When it references a single base table without GROUP BY, aggregate functions, DISTINCT, UNION, or window functions"},
            {"id": "B", "text": "Only when the view is materialized on disk"},
            {"id": "C", "text": "Any view is updatable regardless of complexity"},
            {"id": "D", "text": "Views can never be updated under any circumstances"}
        ],
        "correctAnswer": "A",
        "explanation": "An updatable view must map directly to rows and columns of a single base table; clauses like GROUP BY, DISTINCT, or UNION make it impossible for the engine to determine which base row to modify.",
        "difficulty": "hard",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "sql-gen-48",
        "topic": "SQL",
        "subtopic": "Views",
        "question": "What is the purpose of `WITH CHECK OPTION` in an SQL `CREATE VIEW` statement?",
        "options": [
            {"id": "A", "text": "It ensures that any INSERT or UPDATE performed through the view must satisfy the view's WHERE condition, preventing modifications from producing rows invisible to the view"},
            {"id": "B", "text": "It validates syntax before compilation"},
            {"id": "C", "text": "It checks table primary keys for duplicates"},
            {"id": "D", "text": "It creates a backup copy of the view"}
        ],
        "correctAnswer": "A",
        "explanation": "WITH CHECK OPTION rejects any INSERT or UPDATE through the view that would cause the affected row to disappear from the view's query definition (violating the view's WHERE condition).",
        "difficulty": "hard",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "sql-gen-49",
        "topic": "SQL",
        "subtopic": "Transactions & TCL",
        "question": "Which SQL statement sets the transaction isolation level to Serializable for the current session?",
        "options": [
            {"id": "A", "text": "SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;"},
            {"id": "B", "text": "ALTER SESSION LOCK MODE SERIALIZABLE;"},
            {"id": "C", "text": "START TRANSACTION WITH SERIALIZABLE;"},
            {"id": "D", "text": "LOCK TABLE ALL IN SERIALIZABLE MODE;"}
        ],
        "correctAnswer": "A",
        "explanation": "Standard SQL uses `SET TRANSACTION ISOLATION LEVEL <level>;` to specify transaction isolation (e.g. SERIALIZABLE, REPEATABLE READ, READ COMMITTED, READ UNCOMMITTED).",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "sql-gen-50",
        "topic": "SQL",
        "subtopic": "Data Definition (DDL)",
        "question": "What is the difference between `DROP TABLE Customers;` and `DROP TABLE Customers CASCADE;` (or CASCADE CONSTRAINTS)?",
        "options": [
            {"id": "A", "text": "CASCADE automatically drops all referencing foreign key constraints in child tables, allowing the parent table to be deleted without constraint violation errors"},
            {"id": "B", "text": "CASCADE deletes customer data from cloud backups"},
            {"id": "C", "text": "CASCADE prompts the user for confirmation"},
            {"id": "D", "text": "There is no difference; CASCADE is default"}
        ],
        "correctAnswer": "A",
        "explanation": "Attempting to drop a table referenced by active foreign keys fails unless CASCADE is specified, which removes the foreign key constraints from child tables before dropping the table.",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "sql-gen-51",
        "topic": "SQL",
        "subtopic": "Filtering & WHERE Clause",
        "question": "Consider the query: `SELECT * FROM Employees WHERE department_id IN (10, 20, NULL);`. Will an employee with `department_id = NULL` be returned?",
        "options": [
            {"id": "A", "text": "No, because `NULL = NULL` evaluates to UNKNOWN, and WHERE requires a TRUE condition to include a row"},
            {"id": "B", "text": "Yes, because NULL is in the IN list"},
            {"id": "C", "text": "It throws a syntax error"},
            {"id": "D", "text": "Yes, but only if department_id is indexed"}
        ],
        "correctAnswer": "A",
        "explanation": "`department_id IN (10, 20, NULL)` expands to `department_id = 10 OR department_id = 20 OR department_id = NULL`. When department_id is NULL, all comparisons evaluate to UNKNOWN, excluding the row.",
        "difficulty": "hard",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "sql-gen-52",
        "topic": "SQL",
        "subtopic": "Data Manipulation (DML)",
        "question": "How do you insert the results of a SELECT query directly into an already existing table `ArchivedOrders`?",
        "options": [
            {"id": "A", "text": "INSERT INTO ArchivedOrders (id, amount) SELECT id, amount FROM Orders WHERE status = 'Closed';"},
            {"id": "B", "text": "SELECT id, amount INTO ArchivedOrders FROM Orders;"},
            {"id": "C", "text": "INSERT ArchivedOrders VALUES (SELECT * FROM Orders);"},
            {"id": "D", "text": "UPDATE ArchivedOrders FROM Orders;"}
        ],
        "correctAnswer": "A",
        "explanation": "`INSERT INTO target_table (columns) SELECT columns FROM source_table;` is standard SQL for populating an existing table from a query.",
        "difficulty": "easy",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "sql-gen-53",
        "topic": "SQL",
        "subtopic": "Data Definition (DDL)",
        "question": "Which SQL statement creates a unique index named `idx_users_email` on the `email` column of table `Users`?",
        "options": [
            {"id": "A", "text": "CREATE UNIQUE INDEX idx_users_email ON Users(email);"},
            {"id": "B", "text": "ALTER TABLE Users ADD UNIQUE INDEX (email);"},
            {"id": "C", "text": "MAKE INDEX idx_users_email UNIQUE (email);"},
            {"id": "D", "text": "CREATE INDEX idx_users_email ON Users UNIQUE email;"}
        ],
        "correctAnswer": "A",
        "explanation": "The standard SQL DDL syntax to create an index with uniqueness enforcement is `CREATE UNIQUE INDEX <name> ON <table_name>(<column_name>);`.",
        "difficulty": "easy",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "sql-gen-54",
        "topic": "SQL",
        "subtopic": "Window Functions",
        "question": "What is the purpose of the `NTILE(n)` window function in SQL?",
        "options": [
            {"id": "A", "text": "Divides ordered rows within a partition into approximately `n` equal-sized buckets (e.g. quartiles with NTILE(4))"},
            {"id": "B", "text": "Multiplies row numbers by n"},
            {"id": "C", "text": "Selects every n-th row from the table"},
            {"id": "D", "text": "Limits the query result to n rows"}
        ],
        "correctAnswer": "A",
        "explanation": "`NTILE(n)` divides an ordered partition into n buckets numbered 1 to n, assigning each row its corresponding bucket number (e.g., deciles, quartiles).",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "sql-gen-55",
        "topic": "SQL",
        "subtopic": "Window Functions",
        "question": "Which window function returns the relative rank (from 0.0 to 1.0) of a row within a partition?",
        "options": [
            {"id": "A", "text": "PERCENT_RANK()"},
            {"id": "B", "text": "CUME_DIST()"},
            {"id": "C", "text": "RATIO_TO_REPORT()"},
            {"id": "D", "text": "PERCENTILE_CONT()"}
        ],
        "correctAnswer": "A",
        "explanation": "`PERCENT_RANK()` calculates the relative rank of a row using the formula `(rank - 1) / (total_rows - 1)`, returning a decimal between 0 and 1.",
        "difficulty": "hard",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "sql-gen-56",
        "topic": "SQL",
        "subtopic": "GROUP BY & Aggregation",
        "question": "What does the `GROUPING SETS` operator do when used in a `GROUP BY` clause?",
        "options": [
            {"id": "A", "text": "Allows computing multiple different groupings in a single query (e.g. GROUP BY GROUPING SETS ((department), (location), ()))"},
            {"id": "B", "text": "Groups rows by their primary keys only"},
            {"id": "C", "text": "Sorts grouped records in ascending order"},
            {"id": "D", "text": "Removes duplicate groups from output"}
        ],
        "correctAnswer": "A",
        "explanation": "`GROUPING SETS` lets you specify multiple custom grouping specifications in one query pass, acting as an efficient union of several GROUP BY queries.",
        "difficulty": "hard",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "sql-gen-57",
        "topic": "SQL",
        "subtopic": "GROUP BY & Aggregation",
        "question": "What is the difference between `ROLLUP` and `CUBE` extensions in SQL GROUP BY clauses?",
        "options": [
            {"id": "A", "text": "ROLLUP creates hierarchical subtotals (from left to right, plus grand total), while CUBE creates subtotals for ALL possible combinations of specified columns"},
            {"id": "B", "text": "CUBE is for 3D spatial data only"},
            {"id": "C", "text": "ROLLUP removes NULL values while CUBE preserves them"},
            {"id": "D", "text": "There is no difference; they are exact aliases"}
        ],
        "correctAnswer": "A",
        "explanation": "For columns (A, B): ROLLUP produces aggregations for (A, B), (A), and (); CUBE generates all 2^n combinations: (A, B), (A), (B), and ().",
        "difficulty": "hard",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "sql-gen-58",
        "topic": "SQL",
        "subtopic": "Keys & Constraints",
        "question": "Can a foreign key reference a column in another table that is constrained by `UNIQUE` but is NOT the primary key?",
        "options": [
            {"id": "A", "text": "Yes, standard SQL allows a foreign key to reference any candidate key, including columns with a UNIQUE constraint"},
            {"id": "B", "text": "No, a foreign key can strictly and only reference a PRIMARY KEY column"},
            {"id": "C", "text": "Only if both tables have fewer than 100 rows"},
            {"id": "D", "text": "Only in SQLite, not in enterprise databases"}
        ],
        "correctAnswer": "A",
        "explanation": "Referential integrity requires that the referenced column has a unique identifier guarantee. In standard SQL, this means either a PRIMARY KEY or a UNIQUE constraint.",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "sql-gen-59",
        "topic": "SQL",
        "subtopic": "Data Types & Constraints",
        "question": "What is the difference between `CHAR(10)` and `VARCHAR(10)` in relational databases?",
        "options": [
            {"id": "A", "text": "CHAR(10) is fixed-length and pads shorter strings with trailing spaces to always occupy 10 characters; VARCHAR(10) is variable-length and only stores the actual string length plus length bytes"},
            {"id": "B", "text": "CHAR(10) cannot store numbers"},
            {"id": "C", "text": "VARCHAR(10) can store up to 10 words, while CHAR(10) stores 10 letters"},
            {"id": "D", "text": "VARCHAR consumes more disk space when strings are 10 characters long"}
        ],
        "correctAnswer": "A",
        "explanation": "CHAR(n) is fixed-width, padding stored strings with spaces up to n bytes. VARCHAR(n) allocates storage dynamically matching the length of the inserted text.",
        "difficulty": "easy",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "sql-gen-60",
        "topic": "SQL",
        "subtopic": "Data Types & Constraints",
        "question": "Why is the `DECIMAL` (or `NUMERIC`) data type preferred over `FLOAT` or `REAL` for storing currency and financial balances in SQL?",
        "options": [
            {"id": "A", "text": "DECIMAL is an exact numeric type with fixed precision and scale, avoiding floating-point rounding errors and precision loss inherent in binary IEEE-754 approximations"},
            {"id": "B", "text": "FLOAT cannot store negative amounts"},
            {"id": "C", "text": "DECIMAL requires less disk storage than FLOAT"},
            {"id": "D", "text": "FLOAT does not support arithmetic addition"}
        ],
        "correctAnswer": "A",
        "explanation": "FLOAT and REAL use binary floating-point representation which causes fractional rounding inaccuracies (e.g. 0.1 + 0.2 != 0.3). DECIMAL provides exact decimal arithmetic essential for money.",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "sql-gen-61",
        "topic": "SQL",
        "subtopic": "Joins",
        "question": "What query identifies all customers in a `Customers` table who have NEVER placed any orders in an `Orders` table?",
        "options": [
            {"id": "A", "text": "SELECT c.id FROM Customers c LEFT JOIN Orders o ON c.id = o.customer_id WHERE o.id IS NULL;"},
            {"id": "B", "text": "SELECT c.id FROM Customers c INNER JOIN Orders o ON c.id = o.customer_id;"},
            {"id": "C", "text": "SELECT c.id FROM Customers c WHERE c.id = o.customer_id;"},
            {"id": "D", "text": "SELECT c.id FROM Customers c RIGHT JOIN Orders o ON c.id = o.customer_id;"}
        ],
        "correctAnswer": "A",
        "explanation": "The anti-join pattern: A LEFT JOIN produces NULL in right-side columns for unmatched rows. Filtering with `WHERE o.id IS NULL` isolates records having no matching orders.",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "sql-gen-62",
        "topic": "SQL",
        "subtopic": "Subqueries",
        "question": "Which SQL operator tests whether a subquery returns ANY rows, immediately stopping evaluation as soon as a single match is found?",
        "options": [
            {"id": "A", "text": "EXISTS"},
            {"id": "B", "text": "CONTAINS"},
            {"id": "C", "text": "MATCHES"},
            {"id": "D", "text": "SOME"}
        ],
        "correctAnswer": "A",
        "explanation": "`EXISTS (subquery)` evaluates to TRUE as soon as the first matching row is encountered (short-circuit boolean check), making it highly efficient.",
        "difficulty": "easy",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "sql-gen-63",
        "topic": "SQL",
        "subtopic": "String & Date Functions",
        "question": "What does `SUBSTRING('Database', 1, 4)` (or `SUBSTR`) return in SQL?",
        "options": [
            {"id": "A", "text": "'Data'"},
            {"id": "B", "text": "'base'"},
            {"id": "C", "text": "'atab'"},
            {"id": "D", "text": "'Dat'"}
        ],
        "correctAnswer": "A",
        "explanation": "In standard SQL, string indices are 1-based. Starting at position 1 for a length of 4 characters extracts 'D-a-t-a'.",
        "difficulty": "easy",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "sql-gen-64",
        "topic": "SQL",
        "subtopic": "Transactions & TCL",
        "question": "What is an 'Autonomous Transaction' supported in enterprise database systems (such as Oracle and PostgreSQL)?",
        "options": [
            {"id": "A", "text": "An independent transaction started within the context of a parent transaction that can commit or rollback without affecting the parent transaction"},
            {"id": "B", "text": "A transaction executed automatically by cron without user login"},
            {"id": "C", "text": "A transaction that cannot be canceled once started"},
            {"id": "D", "text": "A transaction that bypasses write-ahead logging"}
        ],
        "correctAnswer": "A",
        "explanation": "An autonomous transaction suspends the calling transaction, executes independent DML, and commits or rolls back independently, making it useful for audit logging even if the main transaction aborts.",
        "difficulty": "hard",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "sql-gen-65",
        "topic": "SQL",
        "subtopic": "Data Definition (DDL)",
        "question": "What is the purpose of the `MERGE` statement (also known as 'UPSERT') in SQL?",
        "options": [
            {"id": "A", "text": "Conditionally inserts new rows or updates existing rows in a target table based on whether matching records exist in a source table"},
            {"id": "B", "text": "Merges two separate database server instances into one"},
            {"id": "C", "text": "Combines two partitions into one disk block"},
            {"id": "D", "text": "Deletes duplicate rows from a single table"}
        ],
        "correctAnswer": "A",
        "explanation": "`MERGE INTO target USING source ON condition WHEN MATCHED THEN UPDATE ... WHEN NOT MATCHED THEN INSERT ...` performs atomic insert-or-update (UPSERT) operations.",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "sql-gen-66",
        "topic": "SQL",
        "subtopic": "Basic Queries & SELECT",
        "question": "What will `SELECT DISTINCT country, city FROM Customers;` return?",
        "options": [
            {"id": "A", "text": "Distinct combinations of country and city together"},
            {"id": "B", "text": "Distinct countries only, with arbitrary cities"},
            {"id": "C", "text": "Distinct cities only, ignoring country"},
            {"id": "D", "text": "A syntax error because DISTINCT only takes one column"}
        ],
        "correctAnswer": "A",
        "explanation": "DISTINCT applies across all columns in the SELECT clause, eliminating duplicate rows where the tuple (country, city) is identical.",
        "difficulty": "easy",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "sql-gen-67",
        "topic": "SQL",
        "subtopic": "Filtering & WHERE Clause",
        "question": "In SQL, what is the operator precedence between `AND` and `OR` when parentheses are omitted?",
        "options": [
            {"id": "A", "text": "`AND` has higher precedence than `OR` (evaluated first)"},
            {"id": "B", "text": "`OR` has higher precedence than `AND`"},
            {"id": "C", "text": "They have identical precedence and evaluate strictly left-to-right"},
            {"id": "D", "text": "Omitting parentheses causes a syntax error"}
        ],
        "correctAnswer": "A",
        "explanation": "In SQL boolean evaluation, AND has higher precedence than OR. `A OR B AND C` is evaluated as `A OR (B AND C)`.",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "sql-gen-68",
        "topic": "SQL",
        "subtopic": "Indexing & Query Performance",
        "question": "What is the danger of creating too many indexes on an Online Transaction Processing (OLTP) database table?",
        "options": [
            {"id": "A", "text": "Every INSERT, UPDATE, and DELETE operation must update all corresponding indexes, slowing down write operations and consuming extra disk and RAM"},
            {"id": "B", "text": "Queries with SELECT are disabled when more than 5 indexes exist"},
            {"id": "C", "text": "Foreign keys stop working if too many indexes are present"},
            {"id": "D", "text": "Indexes overwrite table data after reaching capacity"}
        ],
        "correctAnswer": "A",
        "explanation": "Indexes accelerate read queries, but every modification (INSERT/UPDATE/DELETE) incurs the overhead of updating multiple index trees, degrading write throughput in OLTP workloads.",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "sql-gen-69",
        "topic": "SQL",
        "subtopic": "Aggregate Functions",
        "question": "What is the return value of `COUNT(DISTINCT country)` from a table where `country` contains: 'USA', 'Canada', 'USA', NULL, 'Canada'?",
        "options": [
            {"id": "A", "text": "2"},
            {"id": "B", "text": "3"},
            {"id": "C", "text": "4"},
            {"id": "D", "text": "5"}
        ],
        "correctAnswer": "A",
        "explanation": "COUNT(DISTINCT column) counts distinct non-null values. The distinct values are 'USA' and 'Canada' (2 values); the NULL is ignored.",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "sql-gen-70",
        "topic": "SQL",
        "subtopic": "Conditional Expressions",
        "question": "In standard SQL, which construct allows conditional aggregation to count orders by status inside a single SELECT query?",
        "options": [
            {"id": "A", "text": "SUM(CASE WHEN status = 'Shipped' THEN 1 ELSE 0 END)"},
            {"id": "B", "text": "COUNT(IF status = 'Shipped')"},
            {"id": "C", "text": "WHERE status = 'Shipped' GROUP ALL"},
            {"id": "D", "text": "COUNT() FILTER WHEN status = 'Shipped'"}
        ],
        "correctAnswer": "A",
        "explanation": "`SUM(CASE WHEN condition THEN 1 ELSE 0 END)` (or `COUNT(CASE WHEN condition THEN 1 END)`) is the universal standard SQL pattern for conditional aggregation across multiple categories in one query.",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    }
]
