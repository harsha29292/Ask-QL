-- ORGANIZATIONS

CREATE TABLE organizations (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    industry TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

-- USERS

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    organization_id INT REFERENCES organizations(id),
    name TEXT NOT NULL,
    email TEXT UNIQUE,
    created_at TIMESTAMP DEFAULT NOW()
);

-- TEAMS

CREATE TABLE teams (
    id SERIAL PRIMARY KEY,
    organization_id INT REFERENCES organizations(id),
    name TEXT NOT NULL
);

CREATE TABLE team_members (
    team_id INT REFERENCES teams(id),
    user_id INT REFERENCES users(id),
    PRIMARY KEY(team_id, user_id)
);

-- ROLES

CREATE TABLE roles (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE user_roles (
    user_id INT REFERENCES users(id),
    role_id INT REFERENCES roles(id),
    PRIMARY KEY(user_id, role_id)
);

-- CUSTOMERS

CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    organization_id INT REFERENCES organizations(id),
    name TEXT NOT NULL,
    email TEXT,
    status TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE contacts (
    id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES customers(id),
    name TEXT NOT NULL,
    email TEXT
);

CREATE TABLE leads (
    id SERIAL PRIMARY KEY,
    organization_id INT REFERENCES organizations(id),
    source TEXT,
    status TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

-- DEALS

CREATE TABLE deals (
    id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES customers(id),
    owner_id INT REFERENCES users(id),
    value NUMERIC,
    status TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE activities (
    id SERIAL PRIMARY KEY,
    deal_id INT REFERENCES deals(id),
    user_id INT REFERENCES users(id),
    activity_type TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

-- PROJECTS

CREATE TABLE projects (
    id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES customers(id),
    name TEXT,
    status TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    project_id INT REFERENCES projects(id),
    assigned_user_id INT REFERENCES users(id),
    title TEXT,
    status TEXT,
    due_date DATE
);

CREATE TABLE task_comments (
    id SERIAL PRIMARY KEY,
    task_id INT REFERENCES tasks(id),
    user_id INT REFERENCES users(id),
    comment TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

-- SUPPORT

CREATE TABLE tickets (
    id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES customers(id),
    assigned_user_id INT REFERENCES users(id),
    subject TEXT,
    status TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE ticket_comments (
    id SERIAL PRIMARY KEY,
    ticket_id INT REFERENCES tickets(id),
    user_id INT REFERENCES users(id),
    comment TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

-- BILLING

CREATE TABLE plans (
    id SERIAL PRIMARY KEY,
    name TEXT,
    monthly_price NUMERIC
);

CREATE TABLE subscriptions (
    id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES customers(id),
    plan_id INT REFERENCES plans(id),
    status TEXT,
    start_date DATE,
    end_date DATE
);

CREATE TABLE invoices (
    id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES customers(id),
    amount NUMERIC,
    status TEXT,
    issued_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE payments (
    id SERIAL PRIMARY KEY,
    invoice_id INT REFERENCES invoices(id),
    amount NUMERIC,
    paid_at TIMESTAMP DEFAULT NOW()
);

-- PLATFORM

CREATE TABLE notifications (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    message TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE audit_logs (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    action TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE integrations (
    id SERIAL PRIMARY KEY,
    organization_id INT REFERENCES organizations(id),
    provider TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);