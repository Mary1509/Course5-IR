## Installation
1) Clone repository:
```bash
git clone https://github.com/Mary1509/Course5-IR.git
```
2) Ensure that Docker has been installed on your machine

### Usage
1) Enter repository folder and go to code:
```bash
cd /path/to/repo/cd
```
2) (OPTIONAL) Edit Dockerfile (uncomment and change values)
```bash
# Change to your data if wanted. Originally /data folder is copied to container and can be used
#COPY <path-to-data> /opt/tools/<path-to-data>

# Change to your data if wanted. Originally index program stores files into /opt/tools/results
#COPY <path-to-indexfile> /opt/tools/<path-to-indexfile>
#COPY <path-to-filenames> /opt/tools/<path-to-filenames>
```
3) (OPTIONAL) Edit docker-compose.yml (change run command)
```bash
...
command: ['python3', 'index.py', './data/']   # OR change to <path-to-data>, specified in Dockerfile
...
command: [ 'python3', 'query.py', 'city', '-i', './results/index', '-n', './results/filenames' ]   # OR change to: <word> [-i <index> -n <filenames> -h <help>]
```
4) Build the images:
```bash
docker compose build
```
5Start the containers: 
#### This command will show the logs for the container right in console. If you want to omit it, follow the next step
```bash
docker compose up
```
6) (OPTIONAL) Start the containers in detached mode
```bash
docker compose up -d
```
#### After this you may check the logs of the containers in any convenient way, e.g.
```bash
docker ps -a
docker logs <CONTAINER_ID>
```
7) Stop the containers and remove volume:
```bash
docker compose down -v
```

#### (!!) As the sources is copied on the shared volume of the containers, to recreate and reflect your changes in COPY commands do not forget to remove the volume before new start

## Example of work
```bash
$ docker compose up
[+] Running 4/4
 ✔ Network code_default      Created                                                                                                                                           0.2s 
 ✔ Volume "code_app-volume"  Created                                                                                                                                           0.0s 
 ✔ Container code-index-1    Created                                                                                                                                           0.8s 
 ✔ Container code-query-1    Created                                                                                                                                           0.3s 
Attaching to code-index-1, code-query-1
code-index-1  | [nltk_data] Downloading package stopwords to /root/nltk_data...
code-index-1  | [nltk_data]   Unzipping corpora/stopwords.zip.
code-index-1  | Indexing file /opt/tools/data/input2...
code-index-1  | blend [1, 0, 0]
code-index-1  | bustling [1, 0, 0]
code-index-1  | chatter [1, 0, 0]
code-index-1  | city [11, 0, 0]
code-index-1  | citys [1, 0, 0]
code-index-1  | cityscape [1, 0, 0]
code-index-1  | corner [1, 0, 0]
code-index-1  | creating [1, 0, 0]
code-index-1  | dazzled [1, 0, 0]
code-index-1  | defined [1, 0, 0]
code-index-1  | display [1, 0, 0]
code-index-1  | distant [1, 0, 0]
code-index-1  | diversity [1, 0, 0]
code-index-1  | dwellers [1, 0, 0]
code-index-1  | embraced [1, 0, 0]
code-index-1  | energy [1, 0, 0]
code-index-1  | explored [1, 0, 0]
code-index-1  | filled [1, 0, 0]
code-index-1  | honking [1, 0, 0]
code-index-1  | horns [1, 0, 0]
code-index-1  | hum [1, 0, 0]
code-index-1  | laughter [1, 0, 0]
code-index-1  | life [2, 0, 0]
code-index-1  | lights [1, 0, 0]
code-index-1  | making [1, 0, 0]
code-index-1  | mea [1, 0, 0]
code-index-1  | mesmerizing [1, 0, 0]
code-index-1  | modernity [1, 0, 0]
code-index-1  | nature [1, 0, 0]
code-index-1  | night [1, 0, 0]
code-index-1  | parks [1, 0, 0]
code-index-1  | people [2, 0, 0]
code-index-1  | showcased [1, 0, 0]
code-index-1  | sky [1, 0, 0]
code-index-1  | skyscrapers [1, 0, 0]
code-index-1  | sounds [1, 0, 0]
code-index-1  | story [1, 0, 0]
code-index-1  | streets [1, 0, 0]
code-index-1  | surrounded [1, 0, 0]
code-index-1  | symphony [1, 0, 0]
code-index-1  | towering [1, 0, 0]
code-index-1  | unique [1, 0, 0]
code-index-1  | vibrant [1, 0, 0]
code-index-1  | waiting [1, 0, 0]
code-index-1  | walked [1, 0, 0]
code-index-1  | walks [1, 0, 0]
code-index-1  | 
code-index-1  | Indexing file /opt/tools/data/input...
code-index-1  | air [0, 2, 0]
code-index-1  | blend [1, 0, 0]
code-index-1  | brought [0, 1, 0]
code-index-1  | bustling [1, 0, 0]
code-index-1  | buzzed [0, 1, 0]
code-index-1  | ceased [0, 1, 0]
code-index-1  | chatter [1, 0, 0]
code-index-1  | city [11, 4, 0]
code-index-1  | citys [1, 0, 0]
code-index-1  | cityscape [1, 0, 0]
code-index-1  | colors [0, 1, 0]
code-index-1  | connections [0, 1, 0]
code-index-1  | constant [0, 1, 0]
code-index-1  | corner [1, 0, 0]
code-index-1  | creating [1, 0, 0]
code-index-1  | dance [0, 1, 0]
code-index-1  | dazzled [1, 0, 0]
code-index-1  | defined [1, 0, 0]
code-index-1  | display [1, 0, 0]
code-index-1  | distant [1, 0, 0]
code-index-1  | diversity [1, 0, 0]
code-index-1  | dwellers [1, 0, 0]
code-index-1  | embraced [1, 0, 0]
code-index-1  | energy [1, 2, 0]
code-index-1  | everywhere [0, 1, 0]
code-index-1  | existence [0, 2, 0]
code-index-1  | explored [1, 0, 0]
code-index-1  | filled [1, 1, 0]
code-index-1  | honking [1, 0, 0]
code-index-1  | horns [1, 0, 0]
code-index-1  | hum [1, 1, 0]
code-index-1  | laughter [1, 0, 0]
code-index-1  | life [2, 4, 0]
code-index-1  | lights [1, 0, 0]
code-index-1  | making [1, 0, 0]
code-index-1  | mea [1, 0, 0]
code-index-1  | mesmerizing [1, 0, 0]
code-index-1  | modernity [1, 0, 0]
code-index-1  | moments [0, 1, 0]
code-index-1  | nature [1, 0, 0]
code-index-1  | never [0, 1, 0]
code-index-1  | night [1, 0, 0]
code-index-1  | parks [1, 0, 0]
code-index-1  | people [2, 2, 0]
code-index-1  | personalities [0, 1, 0]
code-index-1  | pulsed [0, 1, 0]
code-index-1  | rhythm [0, 1, 0]
code-index-1  | seemed [0, 1, 0]
code-index-1  | showcased [1, 0, 0]
code-index-1  | sky [1, 0, 0]
code-index-1  | skyscrapers [1, 0, 0]
code-index-1  | sounds [1, 0, 0]
code-index-1  | stories [0, 1, 0]
code-index-1  | story [1, 0, 0]
code-index-1  | streets [1, 2, 0]
code-index-1  | surrounded [1, 0, 0]
code-index-1  | symphony [1, 0, 0]
code-index-1  | tapestry [0, 1, 0]
code-index-1  | threads [0, 1, 0]
code-index-1  | towering [1, 0, 0]
code-index-1  | truly [0, 1, 0]
code-index-1  | unique [1, 1, 0]
code-index-1  | urban [0, 1, 0]
code-index-1  | vibrant [1, 12, 0]
code-index-1  | waiting [1, 0, 0]
code-index-1  | walked [1, 0, 0]
code-index-1  | walks [1, 0, 0]
code-index-1  | woven [0, 1, 0]
code-index-1  | 
code-index-1  | Indexing file /opt/tools/data/input1...
code-index-1  | air [0, 2, 0]
code-index-1  | blend [1, 0, 0]
code-index-1  | brought [0, 1, 0]
code-index-1  | bustling [1, 0, 1]
code-index-1  | buzzed [0, 1, 0]
code-index-1  | ceased [0, 1, 0]
code-index-1  | chatter [1, 0, 0]
code-index-1  | city [11, 4, 9]
code-index-1  | citys [1, 0, 1]
code-index-1  | cityscape [1, 0, 2]
code-index-1  | colors [0, 1, 0]
code-index-1  | connections [0, 1, 0]
code-index-1  | constant [0, 1, 0]
code-index-1  | conversations [0, 0, 1]
code-index-1  | corner [1, 0, 0]
code-index-1  | crafting [0, 0, 1]
code-index-1  | cranny [0, 0, 1]
code-index-1  | creating [1, 0, 0]
code-index-1  | dance [0, 1, 0]
code-index-1  | dazzled [1, 0, 0]
code-index-1  | defined [1, 0, 1]
code-index-1  | display [1, 0, 0]
code-index-1  | displayed [0, 0, 1]
code-index-1  | distant [1, 0, 1]
code-index-1  | distinctive [0, 0, 1]
code-index-1  | diversity [1, 0, 1]
code-index-1  | dwellers [1, 0, 0]
code-index-1  | embraced [1, 0, 1]
code-index-1  | energy [1, 2, 0]
code-index-1  | enveloped [0, 0, 1]
code-index-1  | every [0, 0, 1]
code-index-1  | everywhere [0, 1, 0]
code-index-1  | existence [0, 2, 0]
code-index-1  | explored [1, 0, 1]
code-index-1  | featuring [0, 0, 1]
code-index-1  | filled [1, 1, 0]
code-index-1  | fusion [0, 0, 1]
code-index-1  | honking [1, 0, 1]
code-index-1  | horns [1, 0, 1]
code-index-1  | hum [1, 1, 1]
code-index-1  | illuminated [0, 0, 1]
code-index-1  | individuals [0, 0, 1]
code-index-1  | laughter [1, 0, 1]
code-index-1  | life [2, 4, 2]
code-index-1  | lights [1, 0, 1]
code-index-1  | making [1, 0, 0]
code-index-1  | mea [1, 0, 1]
code-index-1  | mesmerizing [1, 0, 1]
code-index-1  | modernity [1, 0, 1]
code-index-1  | moments [0, 1, 0]
code-index-1  | narrative [0, 0, 1]
code-index-1  | nature [1, 0, 1]
code-index-1  | never [0, 1, 0]
code-index-1  | night [1, 0, 1]
code-index-1  | nook [0, 0, 1]
code-index-1  | parks [1, 0, 1]
code-index-1  | people [2, 2, 0]
code-index-1  | personalities [0, 1, 0]
code-index-1  | populated [0, 0, 1]
code-index-1  | pulsed [0, 1, 0]
code-index-1  | residents [0, 0, 1]
code-index-1  | rhythm [0, 1, 0]
code-index-1  | seemed [0, 1, 0]
code-index-1  | showcased [1, 0, 0]
code-index-1  | sky [1, 0, 1]
code-index-1  | skyscrapers [1, 0, 1]
code-index-1  | sounds [1, 0, 1]
code-index-1  | stories [0, 1, 0]
code-index-1  | story [1, 0, 0]
code-index-1  | streets [1, 2, 1]
code-index-1  | strolling [0, 0, 1]
code-index-1  | surrounded [1, 0, 0]
code-index-1  | symphony [1, 0, 1]
code-index-1  | tapestry [0, 1, 0]
code-index-1  | threads [0, 1, 0]
code-index-1  | towering [1, 0, 1]
code-index-1  | truly [0, 1, 0]
code-index-1  | turning [0, 0, 1]
code-index-1  | unique [1, 1, 0]
code-index-1  | urban [0, 1, 1]
code-index-1  | urbanites [0, 0, 1]
code-index-1  | vibrant [1, 12, 1]
code-index-1  | visual [0, 0, 1]
code-index-1  | vitality [0, 0, 1]
code-index-1  | waiting [1, 0, 1]
code-index-1  | walked [1, 0, 0]
code-index-1  | walks [1, 0, 1]
code-index-1  | within [0, 0, 1]
code-index-1  | woven [0, 1, 0]
code-index-1  | 
code-index-1 exited with code 0
code-query-1  | Searching for:  city
code-query-1  | Using index:  ./results/index
code-query-1  | Loading index...
code-query-1  | Searching...
code-query-1  | 11 /opt/tools/data/input2
code-query-1  | 4 /opt/tools/data/input
code-query-1  | 9 /opt/tools/data/input1
code-query-1 exited with code 0

$ docker compose down -v
[+] Running 4/4
 ✔ Container code-query-1  Removed                                                                                                                                             0.0s 
 ✔ Container code-index-1  Removed                                                                                                                                             0.0s 
 ✔ Volume code_app-volume  Removed                                                                                                                                             0.0s 
 ✔ Network code_default    Removed                                                                                                                                             0.1s 
```