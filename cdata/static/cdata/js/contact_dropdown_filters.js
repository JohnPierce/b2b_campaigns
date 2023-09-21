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
    const groupSelect = document.getElementById("id_company_group");
    const officeLocationSelect = document.getElementById("id_company_office");
    console.log(officeLocationSelect);  // This should print the element or null
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
        console.log(officeLocationSelect);  // This should print the element or null
        console.log('after office location console log II')

        /**
         * Fetch groups associated with the selected company and populate the group dropdown.
         * If no groups are found, a default option is added to the dropdown.
         */
        fetch(`/cdata/get-groups-by-company/${companyId}/`)
            .then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }
                return response.json();
            })
            .then(data => {
                console.log(companyId)
                while (groupSelect.firstChild) {
                    groupSelect.firstChild.remove();
                }

                if (data.length === 0) {
                    const option = new Option("No Groups Available", "");
                    groupSelect.appendChild(option);
                } else {
                    data.forEach(group => {
                        const option = new Option(group.name, group.id);
                        groupSelect.appendChild(option);
                    });
                }
            })
            .catch(error => {
                console.error('There was a problem fetching the groups:', error.message);
            });

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
                while (officeLocationSelect.firstChild) {
                    officeLocationSelect.firstChild.remove();
                }

                if (data.length === 0) {
                    const option = new Option("No Office Locations Available", "");
                    officeLocationSelect.appendChild(option);
                } else {
                    data.forEach(office => {
                        const option = new Option(office.name, office.id);
                        officeLocationSelect.appendChild(option);
                    });
                }
            })
            .catch(error => {
                console.error('There was a problem fetching the office locations:', error.message);
            });
    });
})
