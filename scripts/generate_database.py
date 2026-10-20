# 70 High-Quality Database Fundamentals Practice Questions
database_questions = [
    {
        "id": "db-gen-01",
        "topic": "Database Fundamentals",
        "subtopic": "Database Normalization",
        "question": "A table is in First Normal Form (1NF) if and only if:",
        "options": [
            {"id": "A", "text": "All attribute values are atomic (indivisible) and there are no repeating groups or multi-valued attributes"},
            {"id": "B", "text": "Every non-prime attribute is fully functionally dependent on the entire primary key"},
            {"id": "C", "text": "There are no transitive dependencies between non-key attributes"},
            {"id": "D", "text": "For every functional dependency X -> Y, X is a superkey"}
        ],
        "correctAnswer": "A",
        "explanation": "1NF requires that each column contain only atomic values (single values, not sets, lists, or composite records) and each row is unique.",
        "difficulty": "easy",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "db-gen-02",
        "topic": "Database Fundamentals",
        "subtopic": "Database Normalization",
        "question": "Which condition must be met for a relation to be in Second Normal Form (2NF)?",
        "options": [
            {"id": "A", "text": "It is in 1NF and no non-prime attribute is partially dependent on any candidate key (no partial dependencies)"},
            {"id": "B", "text": "It contains no foreign key references"},
            {"id": "C", "text": "It is in 3NF and possesses no multivalued dependencies"},
            {"id": "D", "text": "Every candidate key consists of exactly one single attribute"}
        ],
        "correctAnswer": "A",
        "explanation": "2NF requires 1NF plus eliminating partial dependencies, meaning non-prime attributes must depend on the whole candidate key, not just a subset of a composite key.",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "db-gen-03",
        "topic": "Database Fundamentals",
        "subtopic": "Database Normalization",
        "question": "A relation is in Third Normal Form (3NF) if it is in 2NF and:",
        "options": [
            {"id": "A", "text": "No non-prime attribute is transitively dependent on any candidate key (no transitive dependencies)"},
            {"id": "B", "text": "All attributes are numeric"},
            {"id": "C", "text": "It contains no NULL values in any column"},
            {"id": "D", "text": "Every relationship is strictly one-to-one"}
        ],
        "correctAnswer": "A",
        "explanation": "3NF removes transitive dependencies (e.g. A -> B and B -> C, where C depends on A through non-key attribute B). Non-key attributes must depend directly and only on candidate keys.",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "db-gen-04",
        "topic": "Database Fundamentals",
        "subtopic": "Database Normalization",
        "question": "What is the defining condition of Boyce-Codd Normal Form (BCNF)?",
        "options": [
            {"id": "A", "text": "For every non-trivial functional dependency X -> Y, the determinant X must be a superkey"},
            {"id": "B", "text": "Every attribute must be a foreign key in another table"},
            {"id": "C", "text": "The table must have exactly one candidate key"},
            {"id": "D", "text": "There are no composite primary keys"}
        ],
        "correctAnswer": "A",
        "explanation": "BCNF is a stricter version of 3NF: for every non-trivial functional dependency X -> Y, X must be a superkey. In 3NF, Y could alternatively be a prime attribute, which BCNF disallows.",
        "difficulty": "hard",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "db-gen-05",
        "topic": "Database Fundamentals",
        "subtopic": "Transactions & ACID Properties",
        "question": "Which ACID property guarantees that all operations within a transaction are completed successfully, or none of them are applied at all (all-or-nothing)?",
        "options": [
            {"id": "A", "text": "Atomicity"},
            {"id": "B", "text": "Consistency"},
            {"id": "C", "text": "Isolation"},
            {"id": "D", "text": "Durability"}
        ],
        "correctAnswer": "A",
        "explanation": "Atomicity guarantees that a transaction is treated as a single indivisible unit of work; if any statement fails, the entire transaction is rolled back.",
        "difficulty": "easy",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "db-gen-06",
        "topic": "Database Fundamentals",
        "subtopic": "Transactions & ACID Properties",
        "question": "Which ACID property guarantees that once a transaction commits, its changes survive system crashes or power failures?",
        "options": [
            {"id": "A", "text": "Durability"},
            {"id": "B", "text": "Atomicity"},
            {"id": "C", "text": "Isolation"},
            {"id": "D", "text": "Consistency"}
        ],
        "correctAnswer": "A",
        "explanation": "Durability ensures committed data is written to non-volatile storage (via write-ahead logs and flushed pages) so that it persists across hardware crashes.",
        "difficulty": "easy",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "db-gen-07",
        "topic": "Database Fundamentals",
        "subtopic": "Transactions & ACID Properties",
        "question": "What concurrency phenomenon is known as a 'Dirty Read'?",
        "options": [
            {"id": "A", "text": "Transaction T1 reads data modified by concurrent transaction T2 before T2 has committed, and T2 later rolls back"},
            {"id": "B", "text": "Transaction T1 reads a row, T2 updates that row, and T1 re-reads the row obtaining a different value"},
            {"id": "C", "text": "Transaction T1 executes a range query, T2 inserts a new matching row, and T1 re-executes finding an extra row"},
            {"id": "D", "text": "Two transactions simultaneously write to the same row, overwriting each other"}
        ],
        "correctAnswer": "A",
        "explanation": "A Dirty Read occurs when a transaction reads uncommitted changes from another concurrent transaction that may subsequently abort and roll back.",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "db-gen-08",
        "topic": "Database Fundamentals",
        "subtopic": "Transactions & ACID Properties",
        "question": "Which ANSI SQL transaction isolation level prevents Dirty Reads and Non-Repeatable Reads, but may still allow Phantom Reads?",
        "options": [
            {"id": "A", "text": "Repeatable Read"},
            {"id": "B", "text": "Read Committed"},
            {"id": "C", "text": "Read Uncommitted"},
            {"id": "D", "text": "Serializable"}
        ],
        "correctAnswer": "A",
        "explanation": "Repeatable Read ensures that any row read by the transaction cannot be changed by other transactions, preventing dirty and non-repeatable reads; new rows matching query filters (phantoms) can still appear unless Serializable is used.",
        "difficulty": "hard",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "db-gen-09",
        "topic": "Database Fundamentals",
        "subtopic": "Concurrency Control & Locking",
        "question": "In Two-Phase Locking (2PL), what are the two distinct phases during a transaction's execution?",
        "options": [
            {"id": "A", "text": "Growing Phase (locks acquired, none released) and Shrinking Phase (locks released, none acquired)"},
            {"id": "B", "text": "Read Phase and Write Phase"},
            {"id": "C", "text": "Validation Phase and Commit Phase"},
            {"id": "D", "text": "Locking Phase and Rollback Phase"}
        ],
        "correctAnswer": "A",
        "explanation": "Basic 2PL protocol dictates that a transaction cannot acquire any new lock once it releases its first lock. The growing phase only acquires locks; the shrinking phase only releases locks.",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "db-gen-10",
        "topic": "Database Fundamentals",
        "subtopic": "Concurrency Control & Locking",
        "question": "What is the key rule that distinguishes Strict Two-Phase Locking (Strict 2PL) from basic 2PL?",
        "options": [
            {"id": "A", "text": "All exclusive (write) locks obtained by a transaction must be held until the transaction terminates (commits or aborts)"},
            {"id": "B", "text": "No shared locks may be obtained at any point"},
            {"id": "C", "text": "All locks are released immediately upon each SQL statement completion"},
            {"id": "D", "text": "Transactions must declare all required locks in advance before starting"}
        ],
        "correctAnswer": "A",
        "explanation": "Strict 2PL prevents cascading aborts by holding all exclusive (X) locks until the transaction's end (COMMIT or ROLLBACK).",
        "difficulty": "hard",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "db-gen-11",
        "topic": "Database Fundamentals",
        "subtopic": "Concurrency Control & Locking",
        "question": "How does a DBMS detect deadlocks in lock-based concurrency systems?",
        "options": [
            {"id": "A", "text": "By maintaining a Wait-For Graph (WFG) and detecting cycles among waiting transactions"},
            {"id": "B", "text": "By calculating the CPU utilization rate of worker threads"},
            {"id": "C", "text": "By counting the number of rows in the buffer pool"},
            {"id": "D", "text": "By checking if foreign keys match primary keys"}
        ],
        "correctAnswer": "A",
        "explanation": "A Wait-For Graph (WFG) represents transactions as vertices and lock dependencies as directed edges. A directed cycle in the graph indicates a circular wait (deadlock).",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "db-gen-12",
        "topic": "Database Fundamentals",
        "subtopic": "Concurrency Control & Locking",
        "question": "In timestamp-based deadlock prevention, what is the policy of the 'Wait-Die' scheme?",
        "options": [
            {"id": "A", "text": "An older transaction is allowed to wait for a younger transaction; a younger transaction dies (aborts) if it requests a lock held by an older transaction"},
            {"id": "B", "text": "The older transaction always aborts immediately"},
            {"id": "C", "text": "Younger transactions preempt and wound older transactions"},
            {"id": "D", "text": "Both transactions abort and rollback"}
        ],
        "correctAnswer": "A",
        "explanation": "In Wait-Die (non-preemptive): if Ti is older than Tj (TS(Ti) < TS(Tj)), Ti is allowed to wait. If Ti is younger (TS(Ti) > TS(Tj)), Ti dies (aborts and restarts with its original timestamp).",
        "difficulty": "hard",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "db-gen-13",
        "topic": "Database Fundamentals",
        "subtopic": "Relational Algebra",
        "question": "Which relational algebra operator filters rows in a relation that satisfy a given selection condition (predicate)?",
        "options": [
            {"id": "A", "text": "Selection (σ)"},
            {"id": "B", "text": "Projection (π)"},
            {"id": "C", "text": "Cartesian Product (×)"},
            {"id": "D", "text": "Natural Join (⨝)"}
        ],
        "correctAnswer": "A",
        "explanation": "Selection (denoted by Greek letter sigma σ) operates horizontally, filtering tuples that satisfy a propositional condition (e.g., σ salary > 50000 (Employee)).",
        "difficulty": "easy",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "db-gen-14",
        "topic": "Database Fundamentals",
        "subtopic": "Relational Algebra",
        "question": "Which relational algebra operator selects specific columns from a relation while eliminating unwanted vertical columns and duplicate rows?",
        "options": [
            {"id": "A", "text": "Projection (π)"},
            {"id": "B", "text": "Selection (σ)"},
            {"id": "C", "text": "Intersection (∩)"},
            {"id": "D", "text": "Division (÷)"}
        ],
        "correctAnswer": "A",
        "explanation": "Projection (denoted by Greek letter pi π) operates vertically, choosing specified attributes and returning a relation with duplicate tuples removed.",
        "difficulty": "easy",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "db-gen-15",
        "topic": "Database Fundamentals",
        "subtopic": "Relational Algebra",
        "question": "If relation R has 10 tuples and relation S has 5 tuples, how many tuples are produced by their Cartesian Product (R × S)?",
        "options": [
            {"id": "A", "text": "50"},
            {"id": "B", "text": "15"},
            {"id": "C", "text": "2"},
            {"id": "D", "text": "10"}
        ],
        "correctAnswer": "A",
        "explanation": "The Cartesian Product of relations with cardinalities n and m produces n * m tuples. Here, 10 * 5 = 50 tuples.",
        "difficulty": "easy",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "db-gen-16",
        "topic": "Database Fundamentals",
        "subtopic": "Relational Algebra",
        "question": "For which relational query is the Relational Division (÷) operator ideally suited?",
        "options": [
            {"id": "A", "text": "Queries with universal quantification, such as finding customers who bought 'ALL' products on a list"},
            {"id": "B", "text": "Calculating the mathematical average of a column"},
            {"id": "C", "text": "Joining tables on primary-foreign key pairs"},
            {"id": "D", "text": "Sorting records in descending order"}
        ],
        "correctAnswer": "A",
        "explanation": "Division (R ÷ S) expresses queries with 'for all' (universal quantification) requirements, identifying tuples in R associated with every tuple in S.",
        "difficulty": "hard",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "db-gen-17",
        "topic": "Database Fundamentals",
        "subtopic": "Storage & Indexing",
        "question": "What is the primary architectural advantage of a B+ Tree over a traditional B-Tree in relational database indexing?",
        "options": [
            {"id": "A", "text": "All data record pointers are stored only in leaf nodes, and leaf nodes are linked sequentially, making range scans exceptionally fast"},
            {"id": "B", "text": "B+ Trees consume zero disk space for non-leaf nodes"},
            {"id": "C", "text": "B+ Trees eliminate the need for primary keys"},
            {"id": "D", "text": "B+ Trees guarantee O(1) constant time lookups"}
        ],
        "correctAnswer": "A",
        "explanation": "In B+ Trees, interior nodes hold only index routing keys; all actual record pointers reside in leaf nodes, which are connected in a doubly linked list for efficient range scans.",
        "difficulty": "hard",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "db-gen-18",
        "topic": "Database Fundamentals",
        "subtopic": "Storage & Indexing",
        "question": "What is a Clustered Index (Primary Index) in an RDBMS?",
        "options": [
            {"id": "A", "text": "An index that defines the actual physical storage order of rows in the table on disk"},
            {"id": "B", "text": "An index created on a temporary in-memory table"},
            {"id": "C", "text": "An index that can be created multiple times per table"},
            {"id": "D", "text": "An index containing only foreign key columns"}
        ],
        "correctAnswer": "A",
        "explanation": "A clustered index determines the physical order of table data on disk pages. Because data rows can only be sorted in one physical sequence, there can be only one clustered index per table.",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "db-gen-19",
        "topic": "Database Fundamentals",
        "subtopic": "ER Modeling",
        "question": "In an Entity-Relationship model, what is a 'Derived Attribute' and how is it typically depicted in Chen ER diagrams?",
        "options": [
            {"id": "A", "text": "An attribute whose value is calculated dynamically from another attribute; represented by a dashed/dotted oval"},
            {"id": "B", "text": "An attribute that forms a primary key; represented by an underlined oval"},
            {"id": "C", "text": "An attribute that can hold multiple values; represented by a double oval"},
            {"id": "D", "text": "An attribute belonging to a weak entity; represented by a double rectangle"}
        ],
        "correctAnswer": "A",
        "explanation": "A derived attribute is computed from existing stored attributes (e.g. calculating Age from DateOfBirth). In Chen notation, it is drawn as a dashed or dotted ellipse.",
        "difficulty": "easy",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "db-gen-20",
        "topic": "Database Fundamentals",
        "subtopic": "ER Modeling",
        "question": "What does 'Total Participation' of an entity in a relationship represent, and how is it graphically represented in ER diagrams?",
        "options": [
            {"id": "A", "text": "Every instance of the entity must participate in at least one relationship instance; depicted by a double line connecting entity to relationship"},
            {"id": "B", "text": "Only some entity instances participate; depicted by a single line"},
            {"id": "C", "text": "The entity contains all primary keys of the database; depicted by a diamond"},
            {"id": "D", "text": "The entity has a one-to-one mapping with all tables; depicted by a dashed line"}
        ],
        "correctAnswer": "A",
        "explanation": "Total participation (existence dependency) mandates that every entity instance must participate in the relationship (e.g., every Loan must belong to a Customer). It is shown as a double line.",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "db-gen-21",
        "topic": "Database Fundamentals",
        "subtopic": "ER Modeling",
        "question": "What is the discriminator (partial key) of a Weak Entity set?",
        "options": [
            {"id": "A", "text": "The set of attributes that distinguishes among weak entity instances that depend on the same identifying strong entity; depicted by a dashed underline"},
            {"id": "B", "text": "A foreign key pointing to an external database"},
            {"id": "C", "text": "A single unique number generated by a sequence"},
            {"id": "D", "text": "The relationship diamond connecting two strong entities"}
        ],
        "correctAnswer": "A",
        "explanation": "A discriminator or partial key differentiates weak entities related to the same owner entity. In ER diagrams, it is indicated with a dashed underline beneath the attribute name.",
        "difficulty": "hard",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "db-gen-22",
        "topic": "Database Fundamentals",
        "subtopic": "Keys & Integrity",
        "question": "What is a 'Surrogate Key' in database design?",
        "options": [
            {"id": "A", "text": "An artificial, system-generated identifier (e.g., auto-increment integer or UUID) with no business meaning, created solely to serve as a primary key"},
            {"id": "B", "text": "A natural key derived from external real-world identifiers like SSN"},
            {"id": "C", "text": "A foreign key that points back to the same table"},
            {"id": "D", "text": "A primary key composed of more than three columns"}
        ],
        "correctAnswer": "A",
        "explanation": "A surrogate key is an artificially created unique key (e.g., sequential integer ID, UUID) having no business semantics, used to simplify joins and indexing over wide composite keys.",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "db-gen-23",
        "topic": "Database Fundamentals",
        "subtopic": "Keys & Integrity",
        "question": "What is the difference between a Candidate Key and an Alternate Key?",
        "options": [
            {"id": "A", "text": "Candidate keys are all minimal superkeys; the one chosen as primary is the Primary Key, and the unchosen ones are Alternate Keys"},
            {"id": "B", "text": "Alternate keys can contain duplicates while candidate keys cannot"},
            {"id": "C", "text": "Candidate keys are foreign keys; alternate keys are indexes"},
            {"id": "D", "text": "There is no difference; the terms are exact synonyms"}
        ],
        "correctAnswer": "A",
        "explanation": "Any minimal superkey qualifies as a Candidate Key. The database designer selects one to be the Primary Key; all other remaining candidate keys are designated as Alternate Keys.",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "db-gen-24",
        "topic": "Database Fundamentals",
        "subtopic": "Database Recovery & Logging",
        "question": "In database crash recovery, what is the Write-Ahead Logging (WAL) protocol?",
        "options": [
            {"id": "A", "text": "Log records describing a data modification must be flushed to non-volatile disk storage BEFORE the corresponding dirty data page is written to disk"},
            {"id": "B", "text": "Data pages are written to disk before log records are recorded"},
            {"id": "C", "text": "Transactions write output directly to client screens before committing"},
            {"id": "D", "text": "Logs are purged immediately upon every commit"}
        ],
        "correctAnswer": "A",
        "explanation": "WAL guarantees Atomicity and Durability: log records recording undo and redo information must reach persistent disk before the modified in-memory data pages overwrite the disk blocks.",
        "difficulty": "hard",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "db-gen-25",
        "topic": "Database Fundamentals",
        "subtopic": "Database Recovery & Logging",
        "question": "What is the purpose of establishing 'Checkpoints' in database management system logs?",
        "options": [
            {"id": "A", "text": "To periodically write modified buffer pages to disk, reducing the amount of log that must be scanned and redone during crash recovery"},
            {"id": "B", "text": "To lock all user tables permanently"},
            {"id": "C", "text": "To reset transaction IDs back to zero"},
            {"id": "D", "text": "To drop unused secondary indexes"}
        ],
        "correctAnswer": "A",
        "explanation": "Checkpoints periodically sync dirty buffer pool pages to disk and write a checkpoint record, bounding recovery time so the recovery engine doesn't have to replay the entire log history from system creation.",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "db-gen-26",
        "topic": "Database Fundamentals",
        "subtopic": "Database Normalization",
        "question": "What is a 'Lossless-Join Decomposition' in relational normalization?",
        "options": [
            {"id": "A", "text": "A decomposition of relation R into R1 and R2 such that natural joining R1 and R2 yields exactly R with no spurious tuples"},
            {"id": "B", "text": "A join operation where no foreign keys are checked"},
            {"id": "C", "text": "A table split where duplicate rows are intentionally created"},
            {"id": "D", "text": "A decomposition that preserves only primary keys"}
        ],
        "correctAnswer": "A",
        "explanation": "A decomposition is lossless if R1 ⨝ R2 = R. If a decomposition is lossy, joining the decomposed tables produces spurious tuples that misrepresent the original data.",
        "difficulty": "hard",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "db-gen-27",
        "topic": "Database Fundamentals",
        "subtopic": "Database Normalization",
        "question": "Why might a database architect intentionally choose to 'Denormalize' a schema in production?",
        "options": [
            {"id": "A", "text": "To improve read performance by reducing expensive multi-table JOIN operations at query time"},
            {"id": "B", "text": "To reduce overall disk storage requirements"},
            {"id": "C", "text": "To eliminate the need for primary keys"},
            {"id": "D", "text": "To ensure 100% adherence to BCNF"}
        ],
        "correctAnswer": "A",
        "explanation": "Denormalization introduces controlled redundancy to optimize analytical or high-read query performance, avoiding costly joins at the cost of additional write overhead and potential update anomalies.",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "db-gen-28",
        "topic": "Database Fundamentals",
        "subtopic": "Relational Model Concepts",
        "question": "What is 'Cardinality' of a relation in relational database theory?",
        "options": [
            {"id": "A", "text": "The total number of tuples (rows) in the relation"},
            {"id": "B", "text": "The total number of attributes (columns) in the relation"},
            {"id": "C", "text": "The maximum length of a string in the table"},
            {"id": "D", "text": "The number of primary keys defined"}
        ],
        "correctAnswer": "A",
        "explanation": "In relational model terminology, Cardinality is the number of rows/tuples in a table, whereas Degree (or Arity) is the number of columns/attributes.",
        "difficulty": "easy",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "db-gen-29",
        "topic": "Database Fundamentals",
        "subtopic": "Relational Model Concepts",
        "question": "What is the 'Degree' (or Arity) of a relation in relational database theory?",
        "options": [
            {"id": "A", "text": "The number of attributes (columns) in the relation"},
            {"id": "B", "text": "The number of rows (tuples) in the relation"},
            {"id": "C", "text": "The depth of the B-tree index"},
            {"id": "D", "text": "The number of foreign keys in the database"}
        ],
        "correctAnswer": "A",
        "explanation": "Degree (or arity) refers to the count of attributes/columns forming the relation schema.",
        "difficulty": "easy",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "db-gen-30",
        "topic": "Database Fundamentals",
        "subtopic": "Transactions & ACID Properties",
        "question": "What is the phenomenon of a 'Lost Update' in concurrent database execution?",
        "options": [
            {"id": "A", "text": "Two concurrent transactions read the same record and write back new values; the second write overwrites the first without incorporating its changes"},
            {"id": "B", "text": "A transaction writes to disk but the power fails before verification"},
            {"id": "C", "text": "A row is deleted accidentally by an administrator"},
            {"id": "D", "text": "A rollback fails to restore table values"}
        ],
        "correctAnswer": "A",
        "explanation": "A Lost Update happens when transaction T1 updates a row based on an initial read, but concurrent transaction T2 overwrites T1's update with its own value, effectively destroying T1's changes.",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "db-gen-31",
        "topic": "Database Fundamentals",
        "subtopic": "Concurrency Control & Locking",
        "question": "Which lock compatibility rule applies between Shared (S) locks and Exclusive (X) locks?",
        "options": [
            {"id": "A", "text": "Multiple transactions can hold Shared locks concurrently on the same item, but an Exclusive lock requires that no other lock (S or X) is held"},
            {"id": "B", "text": "Multiple transactions can hold Exclusive locks simultaneously"},
            {"id": "C", "text": "A Shared lock conflicts with other Shared locks"},
            {"id": "D", "text": "Exclusive locks can only be placed on table primary keys"}
        ],
        "correctAnswer": "A",
        "explanation": "Shared (read) locks are mutually compatible with other shared locks. Exclusive (write) locks are incompatible with both shared and exclusive locks on the same data item.",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "db-gen-32",
        "topic": "Database Fundamentals",
        "subtopic": "Relational Algebra",
        "question": "Under what condition can the Set Union (∪) operator be validly applied to two relations R and S in relational algebra?",
        "options": [
            {"id": "A", "text": "R and S must be Union-Compatible (same number of attributes and corresponding compatible data types)"},
            {"id": "B", "text": "R and S must have identical row counts"},
            {"id": "C", "text": "R must be a foreign key reference to S"},
            {"id": "D", "text": "Both relations must have a single column"}
        ],
        "correctAnswer": "A",
        "explanation": "Union compatibility (type compatibility) requires that both relations have the identical degree (number of attributes) and corresponding attributes have compatible domains.",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "db-gen-33",
        "topic": "Database Fundamentals",
        "subtopic": "Storage & Indexing",
        "question": "What is a 'Dense Index' compared to a 'Sparse Index'?",
        "options": [
            {"id": "A", "text": "A dense index has an index entry for every search key value in the data file; a sparse index has entries only for select values (e.g. one per data page)"},
            {"id": "B", "text": "A dense index stores encrypted passwords, sparse indexes store numbers"},
            {"id": "C", "text": "Sparse indexes are only stored in memory, dense indexes on disk"},
            {"id": "D", "text": "A dense index contains duplicate rows"}
        ],
        "correctAnswer": "A",
        "explanation": "A dense index maintains an index record for every search key value in the table, whereas a sparse index contains records for only some search values (typically one entry per disk block).",
        "difficulty": "hard",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "db-gen-34",
        "topic": "Database Fundamentals",
        "subtopic": "DBMS Architecture & Data Independence",
        "question": "In the Three-Schema Architecture, at which schema level do application users and end-user interfaces interact with database views?",
        "options": [
            {"id": "A", "text": "External Schema Level (View Level)"},
            {"id": "B", "text": "Conceptual Schema Level"},
            {"id": "C", "text": "Internal Schema Level"},
            {"id": "D", "text": "Physical Storage Level"}
        ],
        "correctAnswer": "A",
        "explanation": "The External level (View level) describes customized parts of the database that specific user groups are interested in, hiding unrelated enterprise data.",
        "difficulty": "easy",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "db-gen-35",
        "topic": "Database Fundamentals",
        "subtopic": "Keys & Integrity",
        "question": "When a parent row with a Primary Key is deleted, what does the foreign key action 'ON DELETE CASCADE' do?",
        "options": [
            {"id": "A", "text": "Automatically deletes all matching child rows in the referencing table"},
            {"id": "B", "text": "Prevents the parent deletion and throws an integrity error"},
            {"id": "C", "text": "Sets foreign key columns in child rows to NULL"},
            {"id": "D", "text": "Sets foreign key columns in child rows to default values"}
        ],
        "correctAnswer": "A",
        "explanation": "ON DELETE CASCADE propagates the deletion: whenever a referenced row in the parent table is deleted, all referencing rows in child tables are automatically removed.",
        "difficulty": "easy",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "db-gen-36",
        "topic": "Database Fundamentals",
        "subtopic": "Keys & Integrity",
        "question": "When a foreign key is defined with 'ON DELETE SET NULL', what requirement must the child table's foreign key column satisfy?",
        "options": [
            {"id": "A", "text": "The foreign key column must allow NULL values (cannot be constrained with NOT NULL)"},
            {"id": "B", "text": "The column must be the child table's primary key"},
            {"id": "C", "text": "The column must have a UNIQUE index"},
            {"id": "D", "text": "The column must be an auto-incrementing integer"}
        ],
        "correctAnswer": "A",
        "explanation": "If ON DELETE SET NULL is specified, setting child FK values to NULL will fail if that foreign key column is defined with a NOT NULL constraint.",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "db-gen-37",
        "topic": "Database Fundamentals",
        "subtopic": "ER Modeling",
        "question": "How is a Many-to-Many (M:N) relationship between two entities mapped into a Relational Database schema?",
        "options": [
            {"id": "A", "text": "By creating a separate Junction / Associative table containing foreign keys referencing both participating entities' primary keys"},
            {"id": "B", "text": "By adding the primary key of one table into the other table"},
            {"id": "C", "text": "By merging both entities into a single flat file"},
            {"id": "D", "text": "By using a single composite column storing an array of values"}
        ],
        "correctAnswer": "A",
        "explanation": "Relational tables cannot directly model M:N relationships; an associative (junction) table is created, whose composite primary key consists of the foreign keys of both tables.",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "db-gen-38",
        "topic": "Database Fundamentals",
        "subtopic": "Database Normalization",
        "question": "What is an 'Update Anomaly' caused by lack of database normalization?",
        "options": [
            {"id": "A", "text": "When redundant copies of the same fact exist and updating one copy leaves others unchanged, resulting in data inconsistency"},
            {"id": "B", "text": "When the database driver rejects an UPDATE command due to network timeout"},
            {"id": "C", "text": "When updating a row causes an automatic cascade to all other tables"},
            {"id": "D", "text": "When a primary key auto-increments unexpectedly"}
        ],
        "correctAnswer": "A",
        "explanation": "An update anomaly occurs when data redundancy causes data to be stored in multiple locations; modifying the value in one place while missing others creates contradictory records.",
        "difficulty": "easy",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "db-gen-39",
        "topic": "Database Fundamentals",
        "subtopic": "Database Normalization",
        "question": "What is an 'Insertion Anomaly' in unnormalized tables?",
        "options": [
            {"id": "A", "text": "Inability to record a certain fact about an entity without artificially inserting unrelated data for another entity (e.g., unable to add a course without enrolling a student)"},
            {"id": "B", "text": "Failing to insert due to running out of hard drive space"},
            {"id": "C", "text": "Inserting a record that takes longer than 1 second"},
            {"id": "D", "text": "A trigger preventing insert operations"}
        ],
        "correctAnswer": "A",
        "explanation": "An insertion anomaly occurs when attributes of two distinct entities are combined into one table, preventing the recording of one entity without dummy values for the other.",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "db-gen-40",
        "topic": "Database Fundamentals",
        "subtopic": "Database Normalization",
        "question": "What is a 'Deletion Anomaly' in database theory?",
        "options": [
            {"id": "A", "text": "Unintentionally losing vital information about one entity when deleting records of another entity (e.g. deleting the last student enrolled in a course inadvertently erases all course details)"},
            {"id": "B", "text": "A soft delete that marks a row as inactive"},
            {"id": "C", "text": "When a DROP TABLE statement fails due to active connections"},
            {"id": "D", "text": "Accidental deletion of transaction log files"}
        ],
        "correctAnswer": "A",
        "explanation": "A deletion anomaly occurs when removing a tuple removes not just the intended record, but unintended related facts stored alongside it in an unnormalized table.",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "db-gen-41",
        "topic": "Database Fundamentals",
        "subtopic": "Database Normalization",
        "question": "Which inference rule among Armstrong's Axioms states: If X -> Y and Y -> Z, then X -> Z?",
        "options": [
            {"id": "A", "text": "Transitivity Rule"},
            {"id": "B", "text": "Reflexivity Rule"},
            {"id": "C", "text": "Augmentation Rule"},
            {"id": "D", "text": "Decomposition Rule"}
        ],
        "correctAnswer": "A",
        "explanation": "Armstrong's transitivity axiom states that if X determines Y and Y determines Z, then X functionally determines Z (X -> Z).",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "db-gen-42",
        "topic": "Database Fundamentals",
        "subtopic": "Database Normalization",
        "question": "Which Armstrong's Axiom states: If Y is a subset of X, then X -> Y?",
        "options": [
            {"id": "A", "text": "Reflexivity Rule"},
            {"id": "B", "text": "Augmentation Rule"},
            {"id": "C", "text": "Transitivity Rule"},
            {"id": "D", "text": "Pseudotransitivity Rule"}
        ],
        "correctAnswer": "A",
        "explanation": "The reflexivity axiom asserts that any attribute set functionally determines any subset of itself (e.g. {EmpID, Name} -> EmpID). These are known as trivial functional dependencies.",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "db-gen-43",
        "topic": "Database Fundamentals",
        "subtopic": "Transactions & ACID Properties",
        "question": "What is a 'Phantom Read' anomaly in database transactions?",
        "options": [
            {"id": "A", "text": "A transaction executes a query reading a set of rows matching a search condition; a second transaction inserts or deletes matching rows and commits; the first transaction re-executes the query and sees different rows"},
            {"id": "B", "text": "Reading cached memory that has not been saved to disk"},
            {"id": "C", "text": "A query reading corrupted disk sectors"},
            {"id": "D", "text": "Reading an empty table"}
        ],
        "correctAnswer": "A",
        "explanation": "A phantom read occurs when concurrent inserts or deletes alter the set of rows returned by a predicate search when re-evaluated within the same transaction.",
        "difficulty": "hard",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "db-gen-44",
        "topic": "Database Fundamentals",
        "subtopic": "Transactions & ACID Properties",
        "question": "What is the highest and strictest ANSI SQL transaction isolation level?",
        "options": [
            {"id": "A", "text": "Serializable"},
            {"id": "B", "text": "Repeatable Read"},
            {"id": "C", "text": "Read Committed"},
            {"id": "D", "text": "Snapshot Isolation"}
        ],
        "correctAnswer": "A",
        "explanation": "Serializable is the highest isolation level. It guarantees that the concurrent execution of transactions produces the exact same state as if they were executed serially (one after another).",
        "difficulty": "easy",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "db-gen-45",
        "topic": "Database Fundamentals",
        "subtopic": "Concurrency Control & Locking",
        "question": "What is the primary difference between a Conflict-Serializable schedule and a View-Serializable schedule?",
        "options": [
            {"id": "A", "text": "All conflict-serializable schedules are view-serializable, but some view-serializable schedules containing blind writes are not conflict-serializable"},
            {"id": "B", "text": "Conflict serializability applies only to read-only queries"},
            {"id": "C", "text": "View serializability can be tested in polynomial time while conflict serializability is NP-complete"},
            {"id": "D", "text": "They are completely unrelated models"}
        ],
        "correctAnswer": "A",
        "explanation": "Conflict serializability is a strict subset of view serializability. Testing conflict serializability is polynomial time (precedence graph cycle detection), whereas testing view serializability is NP-complete.",
        "difficulty": "hard",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "db-gen-46",
        "topic": "Database Fundamentals",
        "subtopic": "Storage & Indexing",
        "question": "What happens during a 'Page Split' in a B+ Tree index?",
        "options": [
            {"id": "A", "text": "When a node exceeds its capacity during an insertion, it allocates a new page, moves half of the key entries to the new page, and propagates the middle key up to the parent"},
            {"id": "B", "text": "The entire database is partitioned across two hard drives"},
            {"id": "C", "text": "The index drops older records to maintain size"},
            {"id": "D", "text": "All leaf node pointers are reset to null"}
        ],
        "correctAnswer": "A",
        "explanation": "When an insertion overflows a B+ tree page, it splits into two balanced half-full pages and promotes the separator key to the parent node, preserving B+ tree balance.",
        "difficulty": "hard",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "db-gen-47",
        "topic": "Database Fundamentals",
        "subtopic": "Storage & Indexing",
        "question": "Why is a Hash Index unsuitable for queries using range operators (e.g., WHERE age BETWEEN 20 AND 30)?",
        "options": [
            {"id": "A", "text": "Hash functions distribute keys randomly across buckets, destroying ordering, making range lookups equivalent to a full table scan"},
            {"id": "B", "text": "Hash indexes cannot index integers"},
            {"id": "C", "text": "Hash indexes only support text wildcards"},
            {"id": "D", "text": "Hash tables cannot store values greater than 255"}
        ],
        "correctAnswer": "A",
        "explanation": "Hash indexes provide O(1) equality lookups (`=`) by hashing keys, but because hash buckets do not preserve sorting or range order, range queries cannot use the index.",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "db-gen-48",
        "topic": "Database Fundamentals",
        "subtopic": "Relational Model Concepts",
        "question": "What is the 'Domain Integrity' constraint in relational database systems?",
        "options": [
            {"id": "A", "text": "Enforces that all values in a column must be valid according to the defined data type, format, range, and allowable values"},
            {"id": "B", "text": "Enforces that primary keys are unique"},
            {"id": "C", "text": "Enforces that foreign keys point to valid parents"},
            {"id": "D", "text": "Ensures that DNS domain names resolve to valid IPs"}
        ],
        "correctAnswer": "A",
        "explanation": "Domain integrity validates that values assigned to an attribute conform to its underlying data type, nullability, check constraints, and permissible values.",
        "difficulty": "easy",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "db-gen-49",
        "topic": "Database Fundamentals",
        "subtopic": "ER Modeling",
        "question": "What is a 'Ternary Relationship' in ER modeling?",
        "options": [
            {"id": "A", "text": "A relationship simultaneously associating three distinct entity types"},
            {"id": "B", "text": "A relationship containing exactly three attributes"},
            {"id": "C", "text": "An entity with three candidate keys"},
            {"id": "D", "text": "A recursive relationship on one entity"}
        ],
        "correctAnswer": "A",
        "explanation": "The degree of a relationship is the number of participating entities. A degree of 3 involves three entities (e.g., Supplier, Project, and Part) and is called Ternary.",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "db-gen-50",
        "topic": "Database Fundamentals",
        "subtopic": "ER Modeling",
        "question": "What is a 'Recursive (Self-Referencing) Relationship' in database design?",
        "options": [
            {"id": "A", "text": "A relationship where the same entity type participates more than once in different roles (e.g. Employee manages Employee)"},
            {"id": "B", "text": "A query that executes recursively until all rows are deleted"},
            {"id": "C", "text": "A foreign key that points to a table in another database"},
            {"id": "D", "text": "A weak entity that references another weak entity"}
        ],
        "correctAnswer": "A",
        "explanation": "A unary (recursive) relationship occurs when an entity relates to instances of itself (e.g., an Employee entity where a 'manager_id' foreign key references another 'employee_id' in the same table).",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "db-gen-51",
        "topic": "Database Fundamentals",
        "subtopic": "Database Recovery & Logging",
        "question": "In the ARIES database recovery algorithm, what are the three sequential phases executed after a system crash?",
        "options": [
            {"id": "A", "text": "Analysis Phase -> Redo Phase -> Undo Phase"},
            {"id": "B", "text": "Scan Phase -> Lock Phase -> Commit Phase"},
            {"id": "C", "text": "Validation Phase -> Write Phase -> Read Phase"},
            {"id": "D", "text": "Undo Phase -> Redo Phase -> Checkpoint Phase"}
        ],
        "correctAnswer": "A",
        "explanation": "ARIES recovery executes: 1) Analysis (reconstructs dirty pages and active transactions from the last checkpoint), 2) Redo (repeats history to re-apply committed changes), 3) Undo (rolls back uncommitted transactions).",
        "difficulty": "hard",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "db-gen-52",
        "topic": "Database Fundamentals",
        "subtopic": "Database Recovery & Logging",
        "question": "What is the purpose of Compensating Log Records (CLRs) written during the Undo phase of crash recovery?",
        "options": [
            {"id": "A", "text": "They log the undo actions themselves so that if the system crashes again during recovery, already undone operations are never repeated"},
            {"id": "B", "text": "They encrypt passwords in the log"},
            {"id": "C", "text": "They calculate transaction latency"},
            {"id": "D", "text": "They delete old backups"}
        ],
        "correctAnswer": "A",
        "explanation": "CLRs record an undo action. By pointing to the previous undone log record (UndoNextLSN), they guarantee that recovery progress is never lost even if repeated crashes happen during recovery.",
        "difficulty": "hard",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "db-gen-53",
        "topic": "Database Fundamentals",
        "subtopic": "Database Normalization",
        "question": "Fourth Normal Form (4NF) specifically eliminates which type of dependency?",
        "options": [
            {"id": "A", "text": "Multi-Valued Dependencies (MVDs)"},
            {"id": "B", "text": "Partial Functional Dependencies"},
            {"id": "C", "text": "Transitive Functional Dependencies"},
            {"id": "D", "text": "Trivial Dependencies"}
        ],
        "correctAnswer": "A",
        "explanation": "4NF addresses relations in BCNF that have multi-valued dependencies (X ->> Y), where independent multi-valued facts are wrongly stored in the same relation.",
        "difficulty": "hard",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "db-gen-54",
        "topic": "Database Fundamentals",
        "subtopic": "Database Normalization",
        "question": "What is Fifth Normal Form (5NF / Project-Join Normal Form) concerned with?",
        "options": [
            {"id": "A", "text": "Join Dependencies (lossless reconstruction through 3 or more projections)"},
            {"id": "B", "text": "Multi-valued dependencies between two attributes"},
            {"id": "C", "text": "Atomic column data types"},
            {"id": "D", "text": "Preventing foreign keys from having NULLs"}
        ],
        "correctAnswer": "A",
        "explanation": "5NF (PJNF) deals with relations that cannot be decomposed into two tables without loss of information, but can be losslessly decomposed into three or more tables based on Join Dependencies.",
        "difficulty": "hard",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "db-gen-55",
        "topic": "Database Fundamentals",
        "subtopic": "Relational Algebra",
        "question": "What does a Theta Join (⨝_θ) in relational algebra do?",
        "options": [
            {"id": "A", "text": "Performs a Cartesian product of two relations followed by a Selection based on an arbitrary boolean comparison condition (θ)"},
            {"id": "B", "text": "Always joins tables strictly on equal column names"},
            {"id": "C", "text": "Calculates the union of all rows in both relations"},
            {"id": "D", "text": "Removes unmatched rows from the right relation only"}
        ],
        "correctAnswer": "A",
        "explanation": "A Theta Join is defined as σ_θ (R × S), where θ is any arbitrary predicate condition containing comparison operators (=, <, >, <=, >=, !=).",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "db-gen-56",
        "topic": "Database Fundamentals",
        "subtopic": "Relational Algebra",
        "question": "What is the distinguishing characteristic of a Natural Join (⨝) compared to a generic Equijoin?",
        "options": [
            {"id": "A", "text": "It automatically equates all columns sharing identical names in both relations and eliminates duplicate join columns in the output"},
            {"id": "B", "text": "It requires the user to manually specify ON table1.id = table2.id"},
            {"id": "C", "text": "It preserves non-matching rows with NULLs"},
            {"id": "D", "text": "It sorts the result in reverse order"}
        ],
        "correctAnswer": "A",
        "explanation": "Natural Join matches all pairs of attributes with the same name across both relations, applies equality comparisons, and removes redundant duplicate attribute columns from the final relation schema.",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "db-gen-57",
        "topic": "Database Fundamentals",
        "subtopic": "Storage & Indexing",
        "question": "What is a 'Composite Index' (Multi-Column Index) and what is the 'Leftmost Prefix' rule?",
        "options": [
            {"id": "A", "text": "An index on multiple columns (A, B, C); queries can only use the index if the WHERE clause includes the leftmost column (A), optionally followed by (B), and (C)"},
            {"id": "B", "text": "An index that only sorts text fields alphabetically"},
            {"id": "C", "text": "An index that must always include the primary key as the rightmost column"},
            {"id": "D", "text": "An index that can only be searched from right to left"}
        ],
        "correctAnswer": "A",
        "explanation": "A composite index on (A, B, C) can satisfy queries filtering on (A), (A, B), or (A, B, C), but cannot be used for queries filtering only on (B) or (C) alone due to the leftmost prefix rule.",
        "difficulty": "hard",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "db-gen-58",
        "topic": "Database Fundamentals",
        "subtopic": "Storage & Indexing",
        "question": "What is an 'Index-Organized Table' (or Clustered Table)?",
        "options": [
            {"id": "A", "text": "A table whose entire data rows are stored directly inside the leaf blocks of its B+ Tree primary key index"},
            {"id": "B", "text": "A table that does not allow secondary indexes"},
            {"id": "C", "text": "A temporary table stored in RAM only"},
            {"id": "D", "text": "A table with no indexes defined"}
        ],
        "correctAnswer": "A",
        "explanation": "In an index-organized table (like MySQL InnoDB primary key clustering), the table data is physically embedded in the leaf nodes of the B+ tree rather than in an unordered heap file.",
        "difficulty": "hard",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "db-gen-59",
        "topic": "Database Fundamentals",
        "subtopic": "Transactions & ACID Properties",
        "question": "How does Multi-Version Concurrency Control (MVCC) eliminate read-write locking conflicts in high-performance RDBMS engines?",
        "options": [
            {"id": "A", "text": "Readers do not block writers and writers do not block readers; readers see a consistent historical snapshot based on transaction timestamps or rollback segments"},
            {"id": "B", "text": "By locking the entire database exclusively whenever an update happens"},
            {"id": "C", "text": "By executing all transactions in single-threaded mode"},
            {"id": "D", "text": "By denying read access to any row that has an active lock"}
        ],
        "correctAnswer": "A",
        "explanation": "MVCC creates multiple versions of records (using undo logs or shadow tuples). Read transactions inspect snapshots corresponding to their start timestamp without acquiring shared read locks.",
        "difficulty": "hard",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "db-gen-60",
        "topic": "Database Fundamentals",
        "subtopic": "Transactions & ACID Properties",
        "question": "What is the purpose of the 'SAVEPOINT' command within an ongoing database transaction?",
        "options": [
            {"id": "A", "text": "It creates an intermediate marker allowing partial rollback to that specific point without canceling the entire transaction"},
            {"id": "B", "text": "It commits the transaction permanently to disk"},
            {"id": "C", "text": "It takes a full snapshot backup of all tables"},
            {"id": "D", "text": "It closes the database connection"}
        ],
        "correctAnswer": "A",
        "explanation": "SAVEPOINT defines a named milestone within a transaction. If an error occurs, the application can issue `ROLLBACK TO SAVEPOINT savepoint_name` without discarding preceding successful work.",
        "difficulty": "easy",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "db-gen-61",
        "topic": "Database Fundamentals",
        "subtopic": "Database Schemas & Instances",
        "question": "What is the difference between a Database Schema and a Database State (Instance)?",
        "options": [
            {"id": "A", "text": "The schema is the static structural design (DDL) and rarely changes, while the state is the dynamic data content currently stored at a specific moment in time"},
            {"id": "B", "text": "The schema is stored in memory, the state is stored on disk"},
            {"id": "C", "text": "The schema changes with every INSERT query"},
            {"id": "D", "text": "They are synonymous terms in relational theory"}
        ],
        "correctAnswer": "A",
        "explanation": "A database schema is the structural definition (intension), defined at design time. The database state/instance is the current collection of data rows (extension) at any point in time.",
        "difficulty": "easy",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "db-gen-62",
        "topic": "Database Fundamentals",
        "subtopic": "Keys & Integrity",
        "question": "Can a Candidate Key contain NULL values in a relational database?",
        "options": [
            {"id": "A", "text": "Yes, an alternate candidate key may contain NULL values unless explicitly marked with a NOT NULL constraint; only the designated Primary Key is strictly forbidden from having NULLs"},
            {"id": "B", "text": "No, candidate keys can never contain NULL under any circumstance"},
            {"id": "C", "text": "Yes, even the Primary Key can have one NULL value"},
            {"id": "D", "text": "Only foreign keys can contain numbers"}
        ],
        "correctAnswer": "A",
        "explanation": "Entity Integrity strictly dictates that Primary Keys cannot be NULL. However, other Candidate Keys (enforced via UNIQUE constraints) can permit NULLs in standard SQL unless NOT NULL is specified.",
        "difficulty": "hard",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "db-gen-63",
        "topic": "Database Fundamentals",
        "subtopic": "ER Modeling",
        "question": "In Crow's Foot ER notation, how is a 'One-to-Many' (1:N) relationship with mandatory participation at both ends visually represented?",
        "options": [
            {"id": "A", "text": "Two vertical hash marks (||) on the 'one' side, and a hash mark with crow's foot (|>|) on the 'many' side"},
            {"id": "B", "text": "A circle and a line on both sides"},
            {"id": "C", "text": "Dotted lines with arrows"},
            {"id": "D", "text": "Two circles on both sides"}
        ],
        "correctAnswer": "A",
        "explanation": "In Crow's Foot: || means 'exactly one' (mandatory one). |< (line + crow's foot) means 'one or more' (mandatory many). A circle indicates optional (0).",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "db-gen-64",
        "topic": "Database Fundamentals",
        "subtopic": "Concurrency Control & Locking",
        "question": "What is 'Cascading Abort' (or Cascading Rollback) in concurrency control, and how does Strict 2PL prevent it?",
        "options": [
            {"id": "A", "text": "When the rollback of one transaction forces the rollback of other dependent transactions that read its uncommitted data; Strict 2PL prevents this by holding write locks until commit"},
            {"id": "B", "text": "When an entire database server crashes due to power outage"},
            {"id": "C", "text": "When a deadlock causes all system transactions to terminate"},
            {"id": "D", "text": "When deleting a parent row cascades to child rows"}
        ],
        "correctAnswer": "A",
        "explanation": "If T1 updates data and uncommits, and T2 reads that data, if T1 aborts, T2 must also abort. Strict 2PL forbids releasing exclusive locks until after commit/abort, ensuring other transactions never read uncommitted data.",
        "difficulty": "hard",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "db-gen-65",
        "topic": "Database Fundamentals",
        "subtopic": "Storage & Indexing",
        "question": "What is the primary role of the Buffer Pool Manager in an RDBMS?",
        "options": [
            {"id": "A", "text": "Managing an in-memory cache of disk pages (using page replacement policies like LRU) to minimize slow physical disk I/O reads and writes"},
            {"id": "B", "text": "Storing SQL user credentials and passwords in RAM"},
            {"id": "C", "text": "Compiling query execution plans into machine code"},
            {"id": "D", "text": "Balancing network packets across multiple NICs"}
        ],
        "correctAnswer": "A",
        "explanation": "The Buffer Pool caches database disk pages in RAM. When a query requests a page, the buffer pool manager serves it from memory (cache hit) or reads it from disk using replacement policies (e.g., LRU).",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "db-gen-66",
        "topic": "Database Fundamentals",
        "subtopic": "Database Normalization",
        "question": "Consider a relation R(A, B, C) with functional dependencies: A -> B and B -> C. What type of dependency does A -> C represent?",
        "options": [
            {"id": "A", "text": "A Transitive Dependency"},
            {"id": "B", "text": "A Partial Dependency"},
            {"id": "C", "text": "A Trivial Dependency"},
            {"id": "D", "text": "A Multi-Valued Dependency"}
        ],
        "correctAnswer": "A",
        "explanation": "Because A determines B and B determines C (and B is not a candidate key), C depends on A through intermediate attribute B. This is the definition of a Transitive Dependency (violating 3NF).",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "db-gen-67",
        "topic": "Database Fundamentals",
        "subtopic": "Database Normalization",
        "question": "Consider relation R(StudentID, CourseID, Grade, CourseName) where Primary Key is (StudentID, CourseID). If CourseID -> CourseName, what anomaly is present?",
        "options": [
            {"id": "A", "text": "Partial Dependency (violates 2NF)"},
            {"id": "B", "text": "Transitive Dependency (violates 3NF)"},
            {"id": "C", "text": "Multi-Valued Dependency (violates 4NF)"},
            {"id": "D", "text": "The relation is already in BCNF"}
        ],
        "correctAnswer": "A",
        "explanation": "CourseName depends only on CourseID, which is a proper subset of the composite primary key (StudentID, CourseID). This partial dependency violates 2NF.",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "db-gen-68",
        "topic": "Database Fundamentals",
        "subtopic": "DBMS Concepts & Architecture",
        "question": "What is a 'Database View' and what is the difference between a Virtual View and a Materialized View?",
        "options": [
            {"id": "A", "text": "A virtual view stores only the SQL query definition and evaluates it dynamically on demand; a materialized view physically stores the computed query result on disk and requires refreshing"},
            {"id": "B", "text": "A virtual view cannot be queried using SELECT"},
            {"id": "C", "text": "Materialized views are stored in memory and deleted when the server stops"},
            {"id": "D", "text": "There is no difference; they are identical in storage and behavior"}
        ],
        "correctAnswer": "A",
        "explanation": "A standard (virtual) view is a stored query definition executed at access time. A Materialized View computes and physically stores the result dataset, improving read performance for complex aggregations.",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "db-gen-69",
        "topic": "Database Fundamentals",
        "subtopic": "DBMS Architecture & Data Independence",
        "question": "Adding an index on a table to improve query performance without changing the applications or logical tables is an example of:",
        "options": [
            {"id": "A", "text": "Physical Data Independence"},
            {"id": "B", "text": "Logical Data Independence"},
            {"id": "C", "text": "External View Decoupling"},
            {"id": "D", "text": "Referential Integrity"}
        ],
        "correctAnswer": "A",
        "explanation": "Physical Data Independence is the capacity to change internal physical storage structures (like adding an index or moving files across disks) without affecting conceptual schema or user applications.",
        "difficulty": "easy",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    },
    {
        "id": "db-gen-70",
        "topic": "Database Fundamentals",
        "subtopic": "DBMS Concepts & Architecture",
        "question": "What is the Query Optimizer's role in a Relational Database Management System?",
        "options": [
            {"id": "A", "text": "Evaluating multiple possible execution plans (evaluating joins, index scans, filter orders) and choosing the one with the lowest estimated cost"},
            {"id": "B", "text": "Formatting SQL queries with proper syntax highlighting and indentation"},
            {"id": "C", "text": "Rewriting table constraints to enforce normalization"},
            {"id": "D", "text": "Allocating network bandwidth to connected client sessions"}
        ],
        "correctAnswer": "A",
        "explanation": "The Query Optimizer analyzes the parsed query tree, consults table and index statistics, generates alternative algebraic plans, and selects the lowest-cost execution plan for the query execution engine.",
        "difficulty": "medium",
        "sourceType": "generated",
        "sourceFile": "AI Practice Bank",
        "reviewStatus": "verified"
    }
]
