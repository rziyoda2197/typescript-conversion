Men sizga TypeScript ni qo'shish uchun JavaScript faylini yozaman. 

```typescript
// User.js
export interface User {
  id: number;
  name: string;
  email: string;
  password: string;
}

// UserRepository.js
export interface UserRepository {
  createUser(user: User): Promise<User>;
  getUser(id: number): Promise<User | null>;
  updateUser(id: number, user: User): Promise<User>;
  deleteUser(id: number): Promise<void>;
}

// UserService.js
export interface UserService {
  createUser(user: User): Promise<User>;
  getUser(id: number): Promise<User | null>;
  updateUser(id: number, user: User): Promise<User>;
  deleteUser(id: number): Promise<void>;
}

// UserController.js
export interface UserController {
  createUser(req: any, res: any): Promise<void>;
  getUser(req: any, res: any): Promise<void>;
  updateUser(req: any, res: any): Promise<void>;
  deleteUser(req: any, res: any): Promise<void>;
}

// App.js
import { UserController } from './UserController';
import { UserService } from './UserService';
import { UserRepository } from './UserRepository';

class App {
  private userController: UserController;
  private userService: UserService;
  private userRepository: UserRepository;

  constructor() {
    this.userController = new UserController();
    this.userService = new UserService();
    this.userRepository = new UserRepository();
  }

  public start(): void {
    this.userController.createUser({}, {});
    this.userController.getUser({}, {});
    this.userController.updateUser({}, {});
    this.userController.deleteUser({}, {});
  }
}

// UserController implementation
class UserControllerImpl implements UserController {
  private userService: UserService;

  constructor() {
    this.userService = new UserServiceImpl();
  }

  public async createUser(req: any, res: any): Promise<void> {
    const user = await this.userService.createUser({ name: 'John Doe', email: 'john.doe@example.com', password: 'password' });
    res.json(user);
  }

  public async getUser(req: any, res: any): Promise<void> {
    const user = await this.userService.getUser(1);
    res.json(user);
  }

  public async updateUser(req: any, res: any): Promise<void> {
    const user = await this.userService.updateUser(1, { name: 'Jane Doe', email: 'jane.doe@example.com', password: 'password' });
    res.json(user);
  }

  public async deleteUser(req: any, res: any): Promise<void> {
    await this.userService.deleteUser(1);
    res.json({ message: 'User deleted successfully' });
  }
}

// UserService implementation
class UserServiceImpl implements UserService {
  private userRepository: UserRepository;

  constructor() {
    this.userRepository = new UserRepositoryImpl();
  }

  public async createUser(user: User): Promise<User> {
    return this.userRepository.createUser(user);
  }

  public async getUser(id: number): Promise<User | null> {
    return this.userRepository.getUser(id);
  }

  public async updateUser(id: number, user: User): Promise<User> {
    return this.userRepository.updateUser(id, user);
  }

  public async deleteUser(id: number): Promise<void> {
    return this.userRepository.deleteUser(id);
  }
}

// UserRepository implementation
class UserRepositoryImpl implements UserRepository {
  public async createUser(user: User): Promise<User> {
    // Create user logic here
    return user;
  }

  public async getUser(id: number): Promise<User | null> {
    // Get user logic here
    return null;
  }

  public async updateUser(id: number, user: User): Promise<User> {
    // Update user logic here
    return user;
  }

  public async deleteUser(id: number): Promise<void> {
    // Delete user logic here
  }
}
```
