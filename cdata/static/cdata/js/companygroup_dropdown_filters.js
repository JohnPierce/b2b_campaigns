/**
 * Function to update fields based on the selected company.
 * @param {string} companyId - The selected company ID.
 * @param {HTMLSelectElement} groupHeadQuartersSelect - The groupHeadQuarters select element.
 * @param {HTMLSelectElement} companyHierParentSelect - The companyHierParent select element.
 * @param {string} selectedGroupHeadquarters - The previously selected groupHeadquarters.
 * @param {string} selectedCompanyHierParent - The previously selected companyHierParent.
 */
function updateFieldsByCompany(companyId, groupHeadQuartersSelect, companyHierParentSelect, selectedGroupHeadquarters, selectedCompanyHierParent) {


    // Fetch and update office locations based on the selected company
    console.log('foo III');
    console.log(selectedCompanyHierParent);
    console.log(selectedGroupHeadquarters);
    fetch(`/cdata/get-office-location-by-company/${companyId}/`)
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            // Store the existing state of the dropdowns
            const existingGroupHeadQuarters = groupHeadQuartersSelect.value;
            const existingCompanyHierParent = companyHierParentSelect.value;

            // Clear the dropdown
            groupHeadQuartersSelect.innerHTML = "";

            if (data.length === 0) {
                const option = new Option("No Office Locations Available for assigning group headquarters", "");
                groupHeadQuartersSelect.appendChild(option);
            } else {
                data.forEach(office => {
                    const option = new Option(office.name, office.id);
                    groupHeadQuartersSelect.appendChild(option);
                });
            }
            // Add the previously selected option to the filter list if it's not already present
            if (selectedGroupHeadquarters && !data.some(office => office.id === selectedGroupHeadquarters)) {
                const option = new Option(selectedGroupHeadquarters, selectedGroupHeadquarters);
                groupHeadQuartersSelect.appendChild(option);
            }

            // Restore the previously selected value
            if (selectedGroupHeadquarters) {
                groupHeadQuartersSelect.value = selectedGroupHeadquarters;
            } else {
                groupHeadQuartersSelect.value = existingGroupHeadQuarters;
            }
        })
        .catch(error => {
            console.error('There was a problem fetching the office locations within company group:', error.message);
        });

    // Fetch and update Company Groups based on the selected company
    fetch(`/hierarchy/get-hier-groups-by-company/${companyId}/`)
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            // Clear the dropdown
            companyHierParentSelect.innerHTML = "";

            // Add an option for selecting no parent (null value)
            const nullOption = new Option("No Parent", ""); // You can use null instead of an empty string if you prefer
            companyHierParentSelect.appendChild(nullOption);            

            if (data.length === 0) {
                const option = new Option("No hierarchical groups available for parenting.", "");
                companyHierParentSelect.appendChild(option);
            } else {
                data.forEach(hier_group => {
                    const option = new Option(hier_group.name, hier_group.id);
                    companyHierParentSelect.appendChild(option);
                });
            }
            // Add the previously selected option to the filter list if it's not already present
            if (selectedCompanyHierParent && !data.some(hier_group => hier_group.id === selectedCompanyHierParent)) {
                const option = new Option(selectedCompanyHierParent, selectedCompanyHierParent);
                companyHierParentSelect.appendChild(option);
            }

            // Restore the previously selected value
            if (selectedCompanyHierParent) {
                companyHierParentSelect.value = selectedCompanyHierParent;
            } else {
                companyHierParentSelect.value = existingCompanyHierParent;
            }
        })
        .catch(error => {
            console.error('There was a problem fetching the company groups for hierarchy:', error.message);
        });
}


// Event listener for the DOMContentLoaded event
document.addEventListener("DOMContentLoaded", function() {
    // Get DOM elements for company, group, and office location select dropdowns
    const companySelect = document.getElementById("id_company");
    const groupHeadQuartersSelect = document.getElementById("id_group_headquarters");
    const companyHierParentSelect = document.getElementById("id_companygrouphierarchy-0-parent");

    // Get the initally selected values (if any)
    const initialCompanyId = companySelect.value;
    const initialGroupHeadquarters = groupHeadQuartersSelect.value;
    const initialCompanyHierParent = companyHierParentSelect.value;
    
    console.log('foo');
    // Event listener for the change event on the company select dropdown
    companySelect.addEventListener("change", function() {
        const companyId = this.value;
        updateFieldsByCompany(companyId, groupHeadQuartersSelect, companyHierParentSelect, initialGroupHeadquarters, initialCompanyHierParent); // Call the update function with the selected company ID and elements
    });



    // Call the update function initially if a company is already selected
    if (initialCompanyId) {
        updateFieldsByCompany(initialCompanyId, groupHeadQuartersSelect, companyHierParentSelect, initialGroupHeadquarters, initialCompanyHierParent);
    }
});
