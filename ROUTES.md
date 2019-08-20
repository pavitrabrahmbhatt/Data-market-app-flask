ROUTES
------

| CRUD TYPE | NAME                 | HTTP verb | PATH              | Purpose                                                 |
|-----------|----------------------|-----------|-------------------|---------------------------------------------------------|
| Show      | Home                 | GET       | /                 | Home/Login                                              |
| Index     | Feed                 | GET       | /feed             | Browse Marketplace                                      |
| Show      | Sample Data          | GET       | /sample           | Display Sample Data Set (stretch)                       |
| Show      | Data Sets List       | GET       | /datalist         | Display Data Sets by Industry and in Alphabetical Order |
| Show      | Profile Page         | GET       | /user._id         | Display data sets purchased and up for sale             |
| Show      | user account details | GET       | /user._id/account | get data for user's account                             |
| Show      | Logout               | GET       | /                 | Log user out                                            |
| Show      | Particular Data Set  | GET       | /data._id         | Display info for one data set                           |
| Create    | Register             | POST      | /register         | Create New Account                                      |
| Create    | Sell Data            | POST      | /sell             | Put data set up for sale on marketplace                 |
| Create    | Purchase             | POST      | /data._id         | Purchase data set                                       |
| Edit      |                      | PUT       | /user._id/account | Update user info and redirect                           |
| Edit      |                      | PUT       | /user._id         | Update data info and redirect                           |
| Delete    |                      | DELETE    | /user._id         | Remove data set from marketplace                        |


