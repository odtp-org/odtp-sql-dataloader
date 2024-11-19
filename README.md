# ODTP SQL to CSV

Dataloader from any SQL database into CSV. Perform custom queries. 

| Tool Info | Links |
| --- | --- |
| Original Tool  | Not applicable. The tool is in this repository.  |
| Current Tool Version  | Not applicable. The tool is in this repository. |


## ODTP command 

```
odtp new odtp-component-entry \
--name odtp-sql-dataloader \
--component-version v0.1.1 \
--repository https://github.com/odtp-org/odtp-sql-dataloader
``` 

## Data sheet

| Parameter | Description | Default Value |
| --- | --- | --- |
| PROTOCOL | SQL PROTOCOL | postgresql |
| HOST | SQL HOST | None |
| PORT | SQL PORT | None |
| DATABASE | SQL database to be queried | None |
| QUERY | Query. Please wrap it between `"`: `"QUERY"`  | None |
| OUTPUT_FILENAME | Output file name | `output.csv` |

### Secrets

| Secrets | Description | Default Value |
| --- | --- | --- |
| LOGIN_USER | User in the SQL database | None |
| PASSWORD | Password in the SQL database | None |

### Input Files

No input file is required

### Output Files

| File/Folder | Description |
| --- | --- | 
| CSV File | CSV file containing the results from the QUERY |


## Tutorial

### How to run this component as docker

Build the dockerfile with:

```bash
docker build -t odtp-sql-dataloader .
```

Copy `.env.dist` in `.env` and fill the variables. Run the following command. Mount the correct volumes for input/output folders. 

```bash
docker run -it --rm \
-v {PATH_TO_YOUR_INPUT_VOLUME}:/odtp/odtp-input \
-v {PATH_TO_YOUR_OUTPUT_VOLUME}:/odtp/odtp-output \
--env-file .env odtp-component
```

### Development

This command will create a test folder with the volumes to be mounted. If you are using Powershell, replace `$(pwd)` by `${PWD}`.

```bash
mkdir test
mkdir test/odtp-input
mkdir test/odtp-output
mkdir test/odtp-logs

docker run -it --rm \
-v $(pwd)/test/odtp-input:/odtp/odtp-input \
-v $(pwd)/test/odtp-output:/odtp/odtp-output \
-v $(pwd)/test/odtp-logs:/odtp/odtp-logs \
-v $(pwd)/app:/odtp/odtp-app --env-file .env --entrypoint bash odtp-sql-dataloader
```

Then in order to run the component, you can execute:

```bash
bash /odtp/odtp-component-client/startup.sh
```

Finally, when you are done, please remove the test folder.

```bash
rm -r test
```


## CHANGELOG

- v0.1.1
    - Client updated to v0.1.2
    - Included github action for dockerhub publishing

- v0.1.0
    - First release
    - Ubuntu fixed at 22.04
    - Python fixed at 3.10

## Developed by: 

SDSC & CSFM