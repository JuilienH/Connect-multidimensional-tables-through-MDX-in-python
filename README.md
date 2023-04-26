## python programming settings
To make the python connector work, a ADOMD.NET file must exist in your local folder. Usually the root path is in Program Files\\Microsoft.NET. If you don't have it, please go to Micrsosoft website to download the specific Analysis Services client library. Here is the link I downloaded my ADOMD file: 
https://learn.microsoft.com/en-us/analysis-services/client-libraries?view=asallproducts-allversions
Once it is downloaded, it is ready to construct the connection string and queries in python environment.
## MDX-query for querying multidimensional tables
MDX query is different from SQL used in traditional relational databases, such as PostgreSQL, MySQL, etc... It is actually simpler as the underlying tables are multidimensional. When we query, be sure what fields go in the column/row. The challenge is usually tied to how much acquaintance you have with the databases. For example, what tables having specific fields interact with another tables.
## Example database: Miscrosoft SQL server Analysis Services
