REASSIGN OWNED BY in450a TO postgres;
REASSIGN OWNED BY in450b TO postgres;
REASSIGN OWNED BY in450c TO postgres;

DROP OWNED BY in450a;
DROP OWNED BY in450b;
DROP OWNED BY in450c;

-- ===============================
-- Cleanup Existing Roles
-- ===============================

DROP ROLE IF EXISTS in450a;
DROP ROLE IF EXISTS in450b;
DROP ROLE IF EXISTS in450c;

-- ===============================
-- Create Roles With Login
-- ===============================

CREATE ROLE in450a WITH LOGIN PASSWORD 'Apass123';
CREATE ROLE in450b WITH LOGIN PASSWORD 'Bpass123';
CREATE ROLE in450c WITH LOGIN PASSWORD 'Cpass123';

-- ===============================
-- Remove All Permissions First
-- ===============================

REVOKE ALL ON TABLE in450a FROM in450a, in450b, in450c;
REVOKE ALL ON TABLE in450b FROM in450a, in450b, in450c;
REVOKE ALL ON TABLE in450c FROM in450a, in450b, in450c;

-- ===============================
-- Grant Permissions
-- ===============================

-- in450a can see ALL tables
GRANT SELECT ON TABLE in450a TO in450a;
GRANT SELECT ON TABLE in450b TO in450a;
GRANT SELECT ON TABLE in450c TO in450a;

-- in450b can only see in450b
GRANT SELECT ON TABLE in450b TO in450b;

-- in450c can only see in450c
GRANT SELECT ON TABLE in450c TO in450c;

GRANT CONNECT ON DATABASE postgres TO in450a;
GRANT CONNECT ON DATABASE postgres TO in450b;
GRANT CONNECT ON DATABASE postgres TO in450c;

GRANT USAGE ON SCHEMA public TO in450a;
GRANT USAGE ON SCHEMA public TO in450b;
GRANT USAGE ON SCHEMA public TO in450c;

ALTER ROLE in450a WITH PASSWORD 'Apass123';
ALTER ROLE in450b WITH PASSWORD 'Bpass123';
ALTER ROLE in450c WITH PASSWORD 'Cpass123';
