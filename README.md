# Here You will find the boilerplate for React+Django project

---

> This boilerplate have React (Frontend) and Django+Django Rest Framework (Backend) integrated together with Webpack.

---

## How to use

> Go to backend folder and run `pip install -r requirements.txt` to install all the dependencies.
>
> > Go to frontend folder and run `npm install` to install all the dependencies.
> >
> > > Go to backend folder and run `python manage.py runserver` to start the server.
> > >
> > > > Go to frontend folder and run `npm start` to start the webpack server.

---

> Edit the `python model` in your favour and run `python manage.py makemigrations` and `python manage.py migrate` to create the database.


---


# My Introduction (Use Remix IDE to run the code)

```Solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract Introduction{

    function decodeHash(bytes memory hash) public pure returns(string memory Name, string memory Github,string memory Email,string memory Website) {

        (Name,Github,Email,Website)=abi.decode(hash, (string ,string,string,string));
    }

    
}
// hash=0x000000000000000000000000000000000000000000000000000000000000008000000000000000000000000000000000000000000000000000000000000000c000000000000000000000000000000000000000000000000000000000000001200000000000000000000000000000000000000000000000000000000000000160000000000000000000000000000000000000000000000000000000000000001352616973756c2049736c616d20526f6e6e696500000000000000000000000000000000000000000000000000000000000000000000000000000000000000002268747470733a2f2f706f7274666f6c696f2d666c326c2e76657263656c2e6170702f0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000013726b7372616973756c40676d61696c2e636f6d00000000000000000000000000000000000000000000000000000000000000000000000000000000000000001f68747470733a2f2f6769746875622e636f6d2f526f6e6e69652d41686d656400

```
