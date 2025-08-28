// Предположим, что у вас есть поле поиска с id="searchInput"
document.addEventListener('DOMContentLoaded', function() {
  const input = document.getElementById('searchInput'); // замените на правильный id
  const table = document.getElementById('phonebookTable');

  input.addEventListener('input', function() {
    filterTable();
  });

  function filterTable() {
    const filter = input.value.toLowerCase();
    const rows = Array.from(table.tBodies[0].rows);


    let currentSubdivision = null;
    let currentDepartment = null;

    // Сначала скрываем все строки
    rows.forEach(row => (row.style.display = 'none'));

    for (let row of rows) {
      if (row.classList.contains('subdivision-row')) {
        // Это заголовок подразделения
        const subdivisionHeader = row.querySelector('h2.subdivision');
        const subdivisionName = subdivisionHeader ? subdivisionHeader.textContent.toLowerCase() : '';

        // Проверяем совпадение
        const matchSubdivision = subdivisionName.includes(filter);
        // Запоминаем состояние
        currentSubdivision = {
          row: row,
          match: matchSubdivision
        };

        // Показываем заголовок, если есть совпадение
        row.style.display = matchSubdivision ? '' : 'none';

        // Обнуляем отдел
        currentDepartment = null;
        continue;
      }

      if (row.classList.contains('department-row')) {
        // Это заголовок отдела
        const departmentHeader = row.querySelector('h3.department');
        const departmentName = departmentHeader ? departmentHeader.textContent.toLowerCase() : '';

        const matchDepartment = departmentName.includes(filter);
        currentDepartment = {
          row: row,
          match: matchDepartment
        };

        row.style.display = matchDepartment ? '' : 'none';

        continue;
      }

      // Это строка с контактом
      const text = row.textContent.toLowerCase();

      // Показываем, если:
      // - контакт совпадает
      // - или внутри выбранного подразделения или отдела
      if (
        text.includes(filter) ||
        (currentSubdivision && currentSubdivision.match) ||
        (currentDepartment && currentDepartment.match)
      ) {
        row.style.display = '';
      }
    }
  };
});