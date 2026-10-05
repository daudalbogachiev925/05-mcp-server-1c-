CREATE VIRTUAL TABLE bsl_fts USING fts5(
    module_name, procedure_name, body
);

CREATE TABLE procedures (
    id INTEGER PRIMARY KEY,
    module_name TEXT,
    procedure_name TEXT,
    signature TEXT,
    body TEXT
);
