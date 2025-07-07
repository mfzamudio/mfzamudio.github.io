CREATE SCHEMA bicycle_store ;
USE bicycle_store;

-- 1. customers
CREATE TABLE bicycle_store.customers (
	customerid INT PRIMARY KEY,
	firstname VARCHAR(50) NOT NULL,
	lastname VARCHAR(50) NOT NULL,
	email VARCHAR(100) UNIQUE NOT NULL, -- unique and format expected xxx@yyy.zz
	phonenumber VARCHAR(15) NOT NULL, -- format expected +xx-yyyyyyyyyy
	address TEXT NOT NULL,
	membership VARCHAR(15),  -- 'No','Basic','Premium'
	city VARCHAR(50) NOT NULL,
	state VARCHAR(50),
	postalcode VARCHAR(15),
	country VARCHAR(50) NOT NULL DEFAULT 'Canada',
	creationdate DATE NOT NULL DEFAULT (CURRENT_DATE),
	CONSTRAINT chk_membership_cust CHECK (membership IN ('No','Basic','Premium')),
	CONSTRAINT chk_mail_cust CHECK (email REGEXP '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'),
	CONSTRAINT chk_phonenumber_cust CHECK (phonenumber REGEXP '^\+[0-9]+[- ]?[0-9]+$')
) COMMENT = 'Table to handle customer information';

-- 2. suppliers
CREATE TABLE bicycle_store.suppliers (
    supplierid INT PRIMARY KEY,
    companyname VARCHAR(100) NOT NULL,
    contactname VARCHAR(100) NOT NULL,
    contactemail VARCHAR(100) UNIQUE NOT NULL, -- unique and format expected xxx@yyy.zz
    contactphone VARCHAR(15),  -- format expected +xx-yyyyyyyyyy
	credit DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
	CONSTRAINT chk_contactemail_supp CHECK (contactemail REGEXP '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'),
	CONSTRAINT chk_contactphone_supp CHECK (contactphone REGEXP '^\+[0-9]+[- ]?[0-9]+$')
) COMMENT = 'Table to handle supplier information';

-- 3. employees
CREATE TABLE bicycle_store.employees (
    employeeid INT PRIMARY KEY,
    firstname VARCHAR(50) NOT NULL,
    lastname VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,  -- unique and format expected xxx@yyy.zz
    phonenumber VARCHAR(15), -- format expected +xx-yyyyyyyyyy
    role VARCHAR(50) NOT NULL,
    hiredate DATE NOT NULL DEFAULT (CURRENT_DATE),
	CONSTRAINT chk_mail_empl CHECK (email REGEXP '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'),
	CONSTRAINT chk_phonenumber_empl CHECK (phonenumber REGEXP '^\+[0-9]+[- ]?[0-9]+$')
) COMMENT = 'Table to handle employee information';

-- 4. bicycles
CREATE TABLE bicycle_store.bicycles (
    bicycleid INT PRIMARY KEY,
    modelname VARCHAR(100) NOT NULL,
    brand VARCHAR(50) NOT NULL,
    type VARCHAR(50) NOT NULL,
    price DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
    stockquantity INT NOT NULL DEFAULT 0,
	modelyear INT NOT NULL, -- format YYYY (1900-2050)
	specifications TEXT,
	photo BLOB,
	ingressdate DATE NOT NULL DEFAULT (CURRENT_DATE),
	supplierid INT,
	CONSTRAINT chk_year_bic CHECK (modelyear BETWEEN 1900 AND 2050),
	FOREIGN KEY (supplierid) REFERENCES bicycle_store.suppliers(supplierid)
) COMMENT = 'Table to store the bicycles available and their basic information';

-- 5. spareparts
CREATE TABLE bicycle_store.spareparts (
    sparepartid INT PRIMARY KEY,
    partname VARCHAR(100) NOT NULL,
    brand VARCHAR(50) NOT NULL,
    price DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
    stockquantity INT NOT NULL DEFAULT 0,
	description TEXT,
	photo BLOB,
	ingressdate DATE NOT NULL DEFAULT (CURRENT_DATE),
	supplierid INT NOT NULL,
	FOREIGN KEY (supplierid) REFERENCES bicycle_store.suppliers(supplierid)
) COMMENT = 'Table to store the spare parts available and their basic information';

-- 6. appointments
CREATE TABLE bicycle_store.appointments (
    appointmentid INT PRIMARY KEY,
    appointmentdate DATETIME NOT NULL DEFAULT (CURRENT_DATE),
    purpose VARCHAR(100) NOT NULL,
    status VARCHAR(50) NOT NULL, -- 'Scheduled','Confirmed','Cancelled', 'Finished'
    customerid INT NOT NULL,
	employeeid INT NOT NULL,
	CONSTRAINT chk_status_app CHECK (status IN ('Scheduled','Confirmed','Cancelled', 'Finished')),
	FOREIGN KEY (customerid) REFERENCES bicycle_store.customers(customerid),
	FOREIGN KEY (employeeid) REFERENCES bicycle_store.employees(employeeid)
) COMMENT = 'Table to manage the appointment for repairs';

-- 7. orders
CREATE TABLE bicycle_store.orders (
    orderid INT PRIMARY KEY,
    orderdate DATETIME NOT NULL,
    totalamount DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
    status VARCHAR(50) NOT NULL DEFAULT 'Pending', -- 'Cancelled','Payed','Pending'
	comments TEXT,
	paymentmethod VARCHAR(50),
	channel VARCHAR(50) NOT NULL DEFAULT 'Store', -- 'Store','App','WebPage', 'Partner'
    customerid INT NOT NULL,
	vendorid INT NOT NULL,
	CONSTRAINT chk_status_or CHECK (status IN ('Cancelled','Payed','Pending')),
	CONSTRAINT chk_channel_or CHECK (channel IN ('Store','App','WebPage', 'Partner')),
	FOREIGN KEY (customerid) REFERENCES bicycle_store.customers(customerid),
    FOREIGN KEY (vendorid) REFERENCES bicycle_store.employees(employeeid)
) COMMENT = 'Table to store the order information';

-- 8. orderdetails
CREATE TABLE bicycle_store.orderdetails (
    orderdetailid INT PRIMARY KEY,
    itemid INT NOT NULL,
    itemtype VARCHAR(20) NOT NULL, -- 'Bicycle' or 'SparePart' or 'Repair'
    quantity INT NOT NULL,
    unitprice DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
    orderid INT NOT NULL,
	sparepartid INT,
	bicycleid INT,
	CONSTRAINT chk_status_od CHECK (itemtype IN ('Bicycle','SparePart','Repair')),
    FOREIGN KEY (orderid) REFERENCES bicycle_store.orders(orderid),
	FOREIGN KEY (sparepartid) REFERENCES bicycle_store.spareparts(sparepartid),
	FOREIGN KEY (bicycleid) REFERENCES bicycle_store.bicycles(bicycleid)
) COMMENT = 'Table to store the order details';

-- 9. repairs
CREATE TABLE bicycle_store.repairs (
    repairid INT PRIMARY KEY,
    problemdescription TEXT NOT NULL,
    status VARCHAR(50) NOT NULL, -- 'Cancelled','Ongoing','Finished'
    repaircost DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
    egressdate DATE NOT NULL DEFAULT (CURRENT_DATE),
	ingressdate DATE NOT NULL DEFAULT (CURRENT_DATE),
	startdatetimerepair DATE DEFAULT (CURRENT_DATE),
	enddatetimerepair DATE DEFAULT (CURRENT_DATE), -- this value must be mayor of the startdatetimerepair
    bicycleid INT NOT NULL,
    customerid INT NOT NULL,
	CONSTRAINT chk_repairtime_rep CHECK (enddatetimerepair >= startdatetimerepair),
    CONSTRAINT chk_status_rep CHECK (status IN ('Cancelled','Ongoing','Finished')),
	FOREIGN KEY (bicycleid) REFERENCES bicycle_store.bicycles(bicycleid),
    FOREIGN KEY (customerid) REFERENCES bicycle_store.customers(customerid)
) COMMENT = 'Table to store the repair information';

-- 10. repairassignments
CREATE TABLE bicycle_store.repairassignments (
    assignmentid INT PRIMARY KEY,
    repairid INT NOT NULL,
    employeeid INT NOT NULL,
    FOREIGN KEY (repairid) REFERENCES bicycle_store.repairs(repairid),
    FOREIGN KEY (employeeid) REFERENCES bicycle_store.employees(employeeid)
) COMMENT = 'Table to store the details of the repair assignment with the technician';


