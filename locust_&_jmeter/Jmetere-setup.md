# Setting up Jmeter
- To work with JMeter JDK setup requires
- download Java using the below link

[text](https://www.oracle.com/in/java/technologies/downloads/#java21)

- Check the Version
```
 java -version
```
## Download Jmeter

[text](https://jmeter.apache.org/download_jmeter.cgi)
    - Download from Binaries either TAR or Zip file (for wsl download Zip)
    - extract
    - goto> bin folder> open cmd and wsl
    - run jmeter.bat (for windows) , jmeter.sh (for linux/mac)

![ui](Images/image-1.png)

- Keep the terminal on to work with Jmeter

![ui](Images/image-2.png)

## Implement Performance Testing

![ui](Images/image-3.png)

![ui](Images/image-4.png)

- right click on Thread Group>add>Sampler>HTTP Request

![ui](Images/image-5.png)

- add protocol, ip, http request, path
- url
```
https://jsonplaceholder.typicode.com/todos
```
Or
```
https://jsonplaceholder.typicode.com/todos
```
![ui](Images/image-6.png)

- for checking result press start icon

![ui](Images/image-7.png)

- after clicking start icon click on warnning icon
![ui](Images/image-8.png)

![ui](Images/image-9.png)

- Another way of checking result

![ui](Images/image-10.png)

![ui](Images/image-11.png)
- click on start button and check result response data
- once it is generated you can save to file as well
- click on configure and browse for file name and save data

## Generate Summary Report

![ui](Images/image-12.png)

- run again and generate summary report

 ![ui](Images/image-13.png)