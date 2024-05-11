const BASE_URL =  'http://localhost:5000'

/* export default statement is used to export a single value (variable, function, or object) as the default export fom a module...
   this allows the BASE_URL variable to be imported in relative files under any name i.e., 'import baseurl from './config.js;'
   if there more than one variable was to be imported from this file then use 'named imports' i.e., 'import {base_url, api_key} from './config.js;'
   */
   export default BASE_URL;