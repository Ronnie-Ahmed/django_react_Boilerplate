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
    string  name ="Raisul Islam Ronnie";
    string  email="rksraisul@gmail.com";
    string myportfolio="https://github.com/Ronnie-Ahmed";
    string mywebsite="https://portfolio-fl2l.vercel.app/";

    function getMyName()public view returns (string memory){
        return name;
    }

    function getMyEmail()public view returns(string memory){
     return email;
    }

    function getMyPortfolio()public view returns(string memory){
     return myportfolio;
    }

    function getMyWebsite()public view returns(string memory){
     return mywebsite;
    }

    function getMyhash()public view returns(bytes32){
     return keccak256(abi.encodePacked(name,email,myportfolio,mywebsite));
    }
}
```
