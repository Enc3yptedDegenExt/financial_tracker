function renderCharts(data) {
    const ctxPie = document.getElementById('expensePie').getContext('2d');
    new Chart(ctxPie, {
        type: 'pie',
        data: {
            labels: ['Housing', 'Food', 'Shopping', 'Groceries', 'Transport', 'Entertainment', 'Medical', 'Loans'],
            datasets: [{
                data: data.expenseBreakdown,
                backgroundColor: ['#4F46E5', '#3B82F6', '#60A5FA', '#93C5FD', '#BFDBFE', '#DBEAFE', '#E0F2FE', '#EFF6FF']
            }]
        }
    });

    const ctxBar = document.getElementById('incomeBar').getContext('2d');
    new Chart(ctxBar, {
        type: 'bar',
        data: {
            labels: ['Income', 'Expenses'],
            datasets: [{
                label: 'Amount',
                data: [data.income, data.expenses],
                backgroundColor: ['#10B981', '#EF4444']
            }]
        }
    });
}
