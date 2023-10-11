/**
 * Function to update EDA Design Flow fields based on the selected top level design flow, subcategory & supplier.
 * @param {HTMLSelectElement} edaDesignFlowSelect- The selected company ID.
 * @param {HTMLSelectElement} edaDesignFlowSubCategorysSelect - The groupHeadQuarters select element.
 * @param {HTMLSelectElement} supplierSelect - The supplier/vendor.
 * @param {HTMLSelectElement} edaSupplierToolSelect - The specific tools, product, IP or service the supplier markets and sells.
 */
 */
function updateEDADesignFlowFields(edaDesignFlowSelect, edaDesignFlowSubCategorySelect, supplierSelect, edaSupplierToolSelect) {
    // Store the existing state of the dropdowns
    const existingEdaDesignFlow = edaDesignFlowSelect.value;
    const existingEdaDesignFlowSubCategory = edaDesignFlowSubCategorySelect.value;
    const existingSupplier = supplierSelect.value;
    const existingEdaSupplierTool = edaSupplierToolSelect.value;

    // Fetch and update office locations based on the selected company
    console.log('foo III');

    fetch(`/eda_design_flow/get-eda-design-flow-subcategorys-by-eda-design-flow/${edaDesignFlowSelect.value}/`)
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            // Clear the dropdown
            edaDesignFlowSubCategorySelect.innerHTML = "";

            if (data.length === 0) {
                const option = new Option("No EDA Design Flow SubCategorys Available for assigning group headquarters", "");
                edaDesignFlowSubCategorySelect.appendChild(option);
            } else {
                data.forEach(edaDesignFlowSubCategory => {
                    const option = new Option(edaDesignFlowSubCategory.name, edaDesignFlowSubCategory.id);
                    edaDesignFlowSubCategorySelect.appendChild(option);
                });
            }
        })
        .catch(error => {
            console.error('There was a problem fetching the EDA Design Flow SubCategorys within EDA Design Flow:', error.message);
        });
    
    // Fetch supplier tool list based on the EDADesign Flow, EDA Design Flow SubCategory and Supplier
    fetch(`/eda_design_flow/get-eda-supplier-tool-by-eda-design-flow/?${edaDesignFlowSelect.value}/${edaDesignFlowSubCategorySelect.value}/${supplierSelect.value}/`)
    fetch(`/cdata/get-office-location-by-company/${companyId}/`)
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
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

            // Append the existing state back to the dropdown
            if (selectedGroupHeadquarters) {
                groupHeadQuartersSelect.value = selectedGroupHeadquarters.value;
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

            // If previously assigned, assigned value back to the dropdown
            if (existingCompanyHierParent) {
                companyHierParentSelect.value = existingCompanyHierParent;
            }
        })
        .catch(error => {
            console.error('There was a problem fetching the company groups for hierarchy:', error.message);
        });
}