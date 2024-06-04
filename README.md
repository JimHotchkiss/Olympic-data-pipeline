* Azure Account Structure
    - Account
    - Subscription
    - Resource Group
    - Resources
        * Account - James Hotchkiss. An account can have multiple Subscription
            - Engineering subscription (example). Inside the subscription, you will have the Resource Group. Resource group will be the logical grouping of Azure resources. 
                * Development Resources (example)
                    - VM Scale Sets (Azure resource)
                    - VNet
                    - Azure SQL
                * Production Resources (example)
                    - VM Scale Sets (Azure resource)
                    - VNet
                    - Azure SQL
            - Marketing subscription (examnple)
                * Marketing Resource Group
                    - Azure SQL
* Azure Services
    - Data Factory - Data integration service that enables you to create, schedule and manage data pipelines for efficient data movement and transformation between various sources and destinations in Azure and beyond. It simplifies ETL and data integration tasks
    - Data Lake Gen 2 - Data lake soluition that combines the capabilities of a data lake with the power of Azure Blob Storage, allowing you to store and analyze large volumes of structured and unsctructured data with enchanced performance, security and analytics capabilities
    - Azure Databricks - Databricks is a unified analytics platform buyilt on top of Apache Spark, designed to help data engineers and data scientists collaborate on big data processing and machine learning tasks. It provides tools for data exploration, data processing and building machine learning models in a collaborative and scalable environment
    - Synapse Analytics - SQL Data Warehouse, is a cloud-based analytics service provided by Microsoft Azure. It combines big data and ata warehousing into a single integrated platform, allowing organizations to analyze and process large volumes of data for business intelligence and data analytics purposes


    * Project Details
        - We'll take the raw data and integrate it into Azure Data Factory
        - Then we'll store the raw data in Azure Data Lake Gem 2
        - We'll preform some basic transformation with Azure Databricks
        - We'll then store the transformed data into Azure Data Lake Gen 2
    
    * Set Azure Store resource
        1. Create storage resource first clicking 'Create a resource' and then clicking on 'Storage accounts'
        2. Create a new 'Resource group'
        3. Create Storgage account name - Note - this will have to be a unique name across the Azure ecosystem
            * olympicdataproject1
        4. Select you Region
            * (US) West US 3
        5. Performace - Keep as 'Standard'
        6. Redundancy - Geo-redundant storage (GRS) - Note - this may change from project to project, as different requirements change
        * Click 'Next'
        7. Select 'Enable hierarchical namespace' - this means that all the folder you store in the resource will have the hierarchical format, like on your computer
        * Click 'Next'
        8. On the 'Networking' tab, don't change anything, atleast for this project
        9. On the 'Data protection' tab, don't chnage anything and select 'Next'
        10. On the 'Encryption' tab, the tutorial doesn't cover this. I'll leave it unchanged, and select 'Next'
        11. On the 'Tags' tab, nothing was changed. Select 'Next'
        12. This opens 'Reviews + create' tab, select 'Create' 
            * This will deploy you storage resource
            * Select 'Go to resource'
* Azure Storage account page
    - Data Storage
        * Containers
            - Select 'Containers' 
            - Select '+ Container' to create a 
            container 
            - Create a name, in this example, 'olympicdatacontainer'
            - Select 'Create'
            - This is where we will store all of our data
            - You can select the data container you just created, olympicdatacontainer, in this case
            - We want to create two directories
                * Raw data - This is where we will store all our raw data for the olympic data project
                * Transformed data
            - Select '+ Add Directory' for each directory you want to create, provide a name and select 'create'
            - Note - This is the data lake we need for this project
        * File shares
        * Queues
        * Tables
* Azure Data Factory - We now want to copy our raw data in to our newly created data lake. We'll search Azure for 'Data Factory'
    - Select 'Create data factory'
        * For 'Resource group', we want to select the project name that we created, in this case, 'olympic-data-project'
        * Provide a name. This appears to be a unique value. In this example, 'olympic-project-data-factory1'
        * Select Region, 'West US', in this case.
            - If you get an error regarding the regions, you can select another region
        * Select 'Next' through the following tabs, in this example
            - Git configuration 
            - Networking
            - Advanced
            - Tags 
            - Review + Create - Select 'Create'
                * Select 'Go to resource'
                * Select 'Launch studio'
        * Select 'Author' from the side panel, to begin ingesting data
            - Select the '+' button, and select the 'Pipeline' option
            - Provide name, in this case 'data-ingestion'
        * 'Activities' panel, in the newly created pipeline, are all the operations you may want to perform on you data
            - 'Copy data' - we drag and drop our 'Copy data' operation into the work panel
            - We want to provide data source, for example, a file or an api, to the copy data operation
* Data Access 
    - In this example, we'll push the data files to a Github repository.
    - Select the file we want, and select the 'Raw' button
