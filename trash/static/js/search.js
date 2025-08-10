const input = document.querySelector('input[type="text"]'); // или конкретный селектор вашего поля
const table = document.getElementById('phonebookTable');

input.addEventListener('input', filterTable);

function filterTable() {
  const filter = input.value.toLowerCase();
  const rows = Array.from(table.tBodies[0].rows);

  let currentSubdivisionRow = null;
  let currentDepartmentRow = null;

  let subdivisionHasMatch = false;
  let departmentHasMatch = false;

  // Скрываем все строки
  rows.forEach(row => row.style.display = 'none');

  for (let row of rows) {
    const th = row.querySelector('th[colspan="7"]');

    if (th) {
      const subdivisionH2 = th.querySelector('h2.subdivision');
      const departmentH3 = th.querySelector('h3.department');

      if (subdivisionH2) {
        // Подразделение
        if (currentSubdivisionRow && subdivisionHasMatch) {
          currentSubdivisionRow.style.display = '';
        }
        currentSubdivisionRow = row;
        subdivisionHasMatch = subdivisionH2.textContent.toLowerCase().includes(filter);
        row.style.display = subdivisionHasMatch ? '' : 'none';

        // Сброс отдела
        if (currentDepartmentRow && departmentHasMatch) {
          currentDepartmentRow.style.display = '';
        }
        currentDepartmentRow = null;
        departmentHasMatch = false;

      } else if (departmentH3) {
        // Отдел
        if (currentDepartmentRow && departmentHasMatch) {
          currentDepartmentRow.style.display = '';
        }
        currentDepartmentRow = row;
        departmentHasMatch = departmentH3.textContent.toLowerCase().includes(filter);
        row.style.display = departmentHasMatch ? '' : 'none';
      }

      continue;
    }

    // Это строка с контактами
    const text = row.textContent.toLowerCase();

    // Показываем строку, если:
    // - контакт совпал с фильтром
    // - или совпало подразделение
    // - или совпал отдел
    if (
      text.includes(filter) ||
      subdivisionHasMatch ||
      departmentHasMatch
    ) {
      row.style.display = '';
      subdivisionHasMatch = true;
      departmentHasMatch = true;
    } else {
      row.style.display = 'none';
    }
  }

  // Показываем последние заголовки, если были совпадения
  if (currentDepartmentRow && departmentHasMatch) {
    currentDepartmentRow.style.display = '';
  }
  if (currentSubdivisionRow && subdivisionHasMatch) {
    currentSubdivisionRow.style.display = '';
  }
}
