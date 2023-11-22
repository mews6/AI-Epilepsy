import { Request, Response, NextFunction } from 'express'

/**
* Middleware function that enhances the request object by adding a `_data` function.
* The `_data` function returns an object containing parameters from `req.params`, `req.query`, and `req.body`.
* @returns {Function} Middleware function to be used in Express routes.
*/
export const request= () => {
  return (req:Request, res: Response, next: NextFunction) => {
    
    next()
  }
}
