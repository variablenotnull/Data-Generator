const domainColumns = {
    netflix: [
        'Name', 'Username', 'Email', 'Subscription Date', 'Payment Method', 
        'Subscription Plan', 'Watch Hours', 'Total Time Watched Today',
        'Last Time Watched', 'Country', 'Language Preference', 'Monthly Spend',
        'Next Billing Date', 'Profile Count', 'Watchlist Count', 'Last Payment Date',
        'Device Type', 'Ratings Given', 'Account Status', 'Preferred Genre',
        'Last Watched Title', 'Device Login History', 'Watch History', 'Auto Renewal Status',
        'Content Recommendations', 'Parental Controls', 'Referral Code Used'
    ],
    spotify: [
        'User Name', 'Email', 'Subscription Type', 'Playlist Names', 'Subscription Start Date',
        'Last Login', 'Total Playtime (in minutes)', 'Favorite Artist', 'Favorite Genre',
        'Device Type', 'Country', 'Language', 'Account Status', 'Next Billing Date',
        'Auto Renewal Status', 'Last Payment Date', 'User ID', 'Device ID',
        'Total Songs Listened', 'Average Songs Per Day', 'Premium User Since', 'Email Verified',
        'Followers Count'
    ],
    amazon: [
        'User Name', 'Order ID', 'Email', 'Order Date', 'Product Name', 'Shipping Address',
        'Payment Method', 'Total Amount', 'Delivery Status', 'Delivery Date',
        'Order Status', 'Product Category', 'Product Rating', 'Return Window',
        'Customer Support Contact', 'Coupon Used', 'Gift Wrap', 'Order Type',
        'Delivery Method', 'Payment Status', 'Is Prime Member', 'Item Quantity',
        'Review Submission Date'
    ],
    apple: [
        'User Name', 'Device Model', 'Subscription Type', 'Purchase Date', 'Account Status',
        'Last Login', 'Total Spend', 'Device OS', 'Next Billing Date', 'Auto Renewal Status',
        'Payment Method', 'Purchase History', 'Location', 'Subscription Start Date',
        'Family Sharing', 'Device Type', 'Feedback', 'Warranty Status', 'Total Apps Downloaded',
        'Account Creation Date', 'Gift Cards Used', 'Device Serial Number'
    ]
};

let currentPage = 1;
let totalPages = 1;
let data = [];
 

document.getElementById('domain').addEventListener('change', function() {
    const selectedDomain = this.value;
    const columnsContainer = document.getElementById('columnsContainer');
    
    // Clear previous checkboxes
    columnsContainer.innerHTML = '';
    
    // Generate checkboxes for the selected domain
    domainColumns[selectedDomain].forEach(column => {
        const label = document.createElement('label');
        const checkbox = document.createElement('input');
        checkbox.type = 'checkbox';
        checkbox.name = 'selectedColumns';
        checkbox.value = column;
        label.appendChild(checkbox);
        label.appendChild(document.createTextNode(column));
        columnsContainer.appendChild(label);
        columnsContainer.appendChild(document.createElement('br'));
    });
});

// Modified data fetching and pagination handling
document.getElementById('dataForm').addEventListener('submit', function(e) {
    e.preventDefault();

    const domain = document.getElementById('domain').value;
    const count = document.getElementById('count').value;
    const selectedColumns = Array.from(document.querySelectorAll('input[name="selectedColumns"]:checked')).map(checkbox => checkbox.value);

    // // Show progress bar
    // document.getElementById('progress').style.width = '0%';

    fetch('/generate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ domain: domain, count: count, selectedColumns: selectedColumns })
    })
    .then(response => response.json())
    .then(fetchedData => {
        data = fetchedData;  // Update the global data variable with new data
        const table = document.getElementById('resultTable');
        const tbody = table.querySelector('tbody');
        const tableHeaders = document.getElementById('tableHeaders');
        const prevButton = document.getElementById('prevPage');
        const nextButton = document.getElementById('nextPage');

        tbody.innerHTML = '';
        tableHeaders.innerHTML = '';

        if (data.length > 0) {
            table.style.display = 'table';
            totalPages = Math.ceil(data.length / 10);  // Assuming 10 rows per page
            currentPage = 1;

            // Create table headers
            selectedColumns.forEach(header => {
                const th = document.createElement('th');
                th.textContent = header;
                tableHeaders.appendChild(th);
            });

            displayPage(data);  // Initially display the first page
            updatePaginationButtons(); // Update button visibility
        } else {
            table.style.display = 'none';
            document.getElementById('result').innerHTML = '<p>No data generated.</p>';
            prevButton.style.display = 'none'; // Hide buttons if no data
            nextButton.style.display = 'none';
        }
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('result').innerHTML = '<p>Error generating data. Please try again.</p>';
    });
});

// Display paginated data
function displayPage(data) {
    const table = document.getElementById('resultTable');
    const tbody = table.querySelector('tbody');
    const selectedColumns = Array.from(document.querySelectorAll('input[name="selectedColumns"]:checked')).map(checkbox => checkbox.value);

    tbody.innerHTML = '';
    const start = (currentPage - 1) * 10;
    const end = start + 10;
    const pageData = data.slice(start, end);

    pageData.forEach(item => {
        const row = document.createElement('tr');
        selectedColumns.forEach(header => {
            const cell = document.createElement('td');
            const key = header.toLowerCase().replace(/\s+/g, '_');
            cell.textContent = item[key] || 'N/A';
            row.appendChild(cell);
        });
        tbody.appendChild(row);
    });

    updatePaginationButtons(); // Update button visibility on page change
}

// Update pagination button visibility
function updatePaginationButtons() {
    const prevButton = document.getElementById('prevPage');
    const nextButton = document.getElementById('nextPage');

    if (data.length > 10) {
        prevButton.style.display = currentPage > 1 ? 'inline-block' : 'none';
        nextButton.style.display = currentPage < totalPages ? 'inline-block' : 'none';
    } else {
        prevButton.style.display = 'none';
        nextButton.style.display = 'none';
    }
}

// Pagination buttons
document.getElementById('prevPage').addEventListener('click', function() {
    if (currentPage > 1) {
        currentPage--;
        displayPage(data);  // Re-render the page
    }
});

document.getElementById('nextPage').addEventListener('click', function() {
    if (currentPage < totalPages) {
        currentPage++;
        displayPage(data);  // Re-render the page
    }
});


// Export all data to Excel

document.getElementById('exportExcelButton').addEventListener('click', function () {
    if (data.length > 0) {
        const selectedColumns = Array.from(document.querySelectorAll('input[name="selectedColumns"]:checked')).map(checkbox => checkbox.value);
        
        // Prepare data for Excel
        const excelData = data.map(item => {
            const row = selectedColumns.map(header => item[header.toLowerCase().replace(/\s+/g, '_')] || '');
            return row;
        });

        // Create the worksheet
        const worksheet = XLSX.utils.aoa_to_sheet([selectedColumns, ...excelData]);

        // Create the workbook
        const workbook = XLSX.utils.book_new();
        XLSX.utils.book_append_sheet(workbook, worksheet, 'Sheet 1');

        // Export to Excel
        XLSX.writeFile(workbook, 'generated_data.xlsx');
    } else {
        alert('No data to export!');
    }
});

document.getElementById('exportCsvButton').addEventListener('click', function () {
    if (data.length > 0) {
        const selectedColumns = Array.from(document.querySelectorAll('input[name="selectedColumns"]:checked')).map(checkbox => checkbox.value);
        
        // Create CSV data
        const csvData = [];
        csvData.push(selectedColumns.join(',')); // Add headers

        // Add data rows
        data.forEach(item => {
            const row = selectedColumns.map(header => {
                const key = header.toLowerCase().replace(/\s+/g, '_');
                return item[key] || 'N/A';
            }).join(',');
            csvData.push(row);
        });

        // Create CSV file
        const csvContent = csvData.join('\n');
        const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
        const link = document.createElement('a');
        link.href = URL.createObjectURL(blob);
        link.download = 'generated_data.csv';
        link.click();
    } else {
        alert('No data to export!');
    }
});

document.getElementById('exportJsonButton').addEventListener('click', function () {
    if (data.length > 0) {
        const jsonData = data.map(item => {
            const selectedColumns = Array.from(document.querySelectorAll('input[name="selectedColumns"]:checked')).map(checkbox => checkbox.value);
            const result = {};
            selectedColumns.forEach(header => {
                const key = header.toLowerCase().replace(/\s+/g, '_');
                result[header] = item[key] || 'N/A';
            });
            return result;
        });

        // Create JSON file
        const jsonContent = JSON.stringify(jsonData, null, 2);
        const blob = new Blob([jsonContent], { type: 'application/json' });
        const link = document.createElement('a');
        link.href = URL.createObjectURL(blob);
        link.download = 'generated_data.json';
        link.click();
    } else {
        alert('No data to export!');
    }
});

document.getElementById('exportXmlButton').addEventListener('click', function () {
    if (data.length > 0) {
        const selectedColumns = Array.from(document.querySelectorAll('input[name="selectedColumns"]:checked')).map(checkbox => checkbox.value);
        
        // Create XML data
        let xmlContent = '<?xml version="1.0" encoding="UTF-8"?>\n<data>\n';
        
        data.forEach(item => {
            xmlContent += '  <row>\n';
            selectedColumns.forEach(header => {
                const key = header.toLowerCase().replace(/\s+/g, '_');
                const value = item[key] || 'N/A';
                xmlContent += `    <${key}>${value}</${key}>\n`;
            });
            xmlContent += '  </row>\n';
        });
        
        xmlContent += '</data>';
        
        // Create XML file
        const blob = new Blob([xmlContent], { type: 'application/xml' });
        const link = document.createElement('a');
        link.href = URL.createObjectURL(blob);
        link.download = 'generated_data.xml';
        link.click();
    } else {
        alert('No data to export!');
    }
});

document.getElementById('exportPdfButton').addEventListener('click', function () {
    if (data.length > 0) {
        const selectedColumns = Array.from(document.querySelectorAll('input[name="selectedColumns"]:checked')).map(checkbox => checkbox.value);
        
        // Initialize jsPDF
        const doc = new jsPDF();
        
        // Add table headers to PDF
        const headers = selectedColumns;
        const rows = data.map(item => {
            return selectedColumns.map(header => {
                const key = header.toLowerCase().replace(/\s+/g, '_');
                return item[key] || 'N/A';
            });
        });

        // Create table in PDF
        doc.autoTable({
            head: [headers],
            body: rows,
        });

        // Download PDF
        doc.save('generated_data.pdf');
    } else {
        alert('No data to export!');
    }
});

document.getElementById('exportSqlButton').addEventListener('click', function () {
    if (data.length > 0) {
        const selectedColumns = Array.from(document.querySelectorAll('input[name="selectedColumns"]:checked')).map(checkbox => checkbox.value);
        
        // SQL insert statement header
        const tableName = "your_table_name";  // Replace with your table name
        let sqlContent = `-- SQL export for ${tableName}\n\n`;
        
        // Loop through the data and create SQL insert statements
        data.forEach(item => {
            let insertStatement = `INSERT INTO ${tableName} (${selectedColumns.join(', ')}) VALUES (`;
            
            const values = selectedColumns.map(header => {
                const key = header.toLowerCase().replace(/\s+/g, '_');
                const value = item[key] || 'NULL'; // Handle null or missing values
                return `'${value}'`;  // Add quotes for string values
            }).join(', ');
            
            insertStatement += values + ');\n';
            sqlContent += insertStatement; // Add the insert statement to SQL content
        });
        
        // Create SQL file
        const blob = new Blob([sqlContent], { type: 'application/sql' });
        const link = document.createElement('a');
        link.href = URL.createObjectURL(blob);
        link.download = 'generated_data.sql';
        link.click();
    } else {
        alert('No data to export!');
    }
});


