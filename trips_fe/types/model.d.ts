export interface TourGuide {
  user: number,
  description: string,
  identification: number,
  email: string,
  address: string,
  telephone: number
}

export interface User {
  id?: number,
  password?: string,
  email?: string,
  tourguide_id?: number
  tourguide?: TourGuide,
  username: string
}

export interface TripAPIError {
  error: string
}

export interface Trip {
  id?: number,
  user_id?: number
  user?: User,
  description: string,
  price: number,
  match: number,
  long_days: number,
  location: string,
  date: Date,
  likes: number
}

export interface Booking {
  trip_id?: number,
  trip?: Trip,
  user: number
}