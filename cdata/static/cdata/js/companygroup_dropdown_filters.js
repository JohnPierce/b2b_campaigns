/**
 * Event listener for the DOMContentLoaded event.
 * This event fires when the initial HTML document has been completely loaded,
 * without waiting for stylesheets, images, and subframes to finish loading.
 */
document.addEventListener("DOMContentLoaded", function() {

    /**
     * Get DOM elements for company, group, and office location select dropdowns.
     * @type {HTMLSelectElement}
     */
    const companySelect = document.getElementById("id_company");
    const groupSelect = document.getElementById("id_name");
    const groupHeadQuartersSelect = document.getElementById("id_group_headquarters");
    const companyHierSelect = document.getElementById("id_companygrouphierarchy-0-company");
    const companyHierParentSelect = document.getElementById("id_companygrouphierarchy-0-parent");
    console.log('after office location console log')


    /**
     * Event listener for the change event on the company select dropdown.
     * This event fires whenever a company is selected, triggering data fetches
     * for the corresponding groups and office locations.
     */
    companySelect.addEventListener("change", function() {
        /**
         * Selected company ID from the dropdown.
         * @type {string}
         */
        const companyId = this.value;
        console.log('Company ID')
        console.log(groupHeadQuartersSelect);  // This should print the element or null
        console.log('after office location console log III')

        /**
         * Fetch office locations associated with the selected company and populate the office location dropdown.
         * If no office locations are found, a default option is added to the dropdown.
         */
        fetch(`/cdata/get-office-location-by-company/${companyId}/`)
            .then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }
                return response.json();
            })
            .then(data => {
                while (groupHeadQuartersSelect.firstChild) {
                    groupHeadQuartersSelect.firstChild.remove();
                }

                if (data.length === 0) {
                    const option = new Option("No Office Locations Available for assigning group headquarters", "");
                    groupHeadQuartersSelect.appendChild(option);
                } else {
                    data.forEach(office => {
                        const option = new Option(office.name, office.id);
                        groupHeadQuartersSelect.appendChild(option);
                    });
                }
            })
            .catch(error => {
                console.error('There was a problem fetching the office locations within company group:', error.message);
            });


        /**
         * Fetch Company Groups defined in the hierarchy app and populate the parent dropdown.
         * If no groups defined in hierarchy, will need to add a group to the hierarchy.
         */
        fetch(`/hierarchy/get-hier-groups-by-company/${companyId}/`)

            .then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }
                return response.json();
            })
            .then(data => {
                while (companyHierParentSelect.firstChild) {
                    companyHierParentSelect.firstChild.remove();
                }

                if (data.length === 0) {
                    const option = new Option("No hierarchical groups available for parenting.", "");
                    companyHierParentSelect.appendChild(option);
                } else {
                    data.forEach(hier_group => {
                        const option = new Option(hier_group.name, hier_group.id);
                        companyHierParentSelect.appendChild(option);
                    });
                }
            })
            .catch(error => {
                console.error('There was a problem fetching the office locations within company group:', error.message);
            });
        console.log('right before the fetch for hierarchical data')
    });
})
