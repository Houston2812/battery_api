# Battery info API
Using this api it is possible to get information about the percentage of the laptop's battery. There exist 4 commands according to the CRUD principle. SQLite database is used in the project. 

## API structure
API consits of 3 endpoint and can perform 5 operatoins.

### Endpoints
 * /api/v1/resources/laptops
 * /api/v1/resources/laptops/<device_name>
 * /api/v1/resources/laptops/status

### Operations
  1. It is possible to get info of the user's laptop _GET_ request is sent to the _/api/v1/resources/laptops_ endpoint?device_name="".\
  The only parameter for this request is name of the device, that is delivered in the request url.
  2. To register new user in the system _POST_ requet is sent to the _/api/v1/resources/laptops_ endpoint. \
  The parameter for this request is name of the device sent in the json format.
  3. To update data of the current user _PUT_ request is sent to the _/api/v1/resources/laptops_ endpoint.\
  The parameters for this json formatted request are:\
       * Name of the device - _device_name_\
       * Charging status - _power_\
       * Charge level - _percentage_\
  4. To the delete current user _DELETE_ request is sent to the _/api/v1/resources/laptops/<device_name>_ endpoint.\
    This request has only one parameter _<device_name>_, that is sent in the request url.
  5. To stop the execution of the software _POST_ request is sent to the _/api/v1/resources/laptops/status_ endpoint.\
    The parameters for this request are:
        * Name of the device - _device_name_
        * Execution status - _status_ 
