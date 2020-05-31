<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Http\Controllers\Controller; 
use App\User; 
use Illuminate\Support\Facades\Auth; 
use Validator;

class UserController extends Controller
{
    public $successStatus = 200;

    /** 
    * Hace una verificación sobre el email y la contraseña, que lo compara contra los datos del usuario y si es exitoso, crea un token y pasa al estado de success.
    * 
    * @return \Illuminate\Http\Response 
    */ 
    public function login(){ 
        if(Auth::attempt(['email' => request('email'), 'password' => request('password')])){ 
        $user = Auth::user(); 
        $success['token'] =  $user->createToken('MyApp')-> accessToken; 
        return response()->json(['success' => $success], $this-> successStatus); 
        } 
        else{ 
        return response()->json(['error'=>'Unauthorised'], 401); 
        } 
    }

    /** 
    * Llama a un validador que valida los campos necesarios para registrar un usuario (name, email, password, confirm password), si los valores son correctos, registrará al usuario y le creará un token. 
    * 
    * @return \Illuminate\Http\Response 
    */ 
    public function register(Request $request) 
    { 
    $validator = Validator::make($request->all(), [ 
    'name' => 'required', 
    'email' => 'required|email', 
    'password' => 'required', 
    'c_password' => 'required|same:password', 
    ]);
    if ($validator->fails()) { 
    return response()->json(['error'=>$validator->errors()], 401);            
    }
    $input = $request->all(); 
    $input['password'] = bcrypt($input['password']); 
    $user = User::create($input); 
    $success['token'] =  $user->createToken('MyApp')-> accessToken; 
    $success['name'] =  $user->name;
    return response()->json(['success'=>$success], $this-> successStatus); 
    }

    /** 
    * details api 
    * 
    * @return \Illuminate\Http\Response 
    */ 
    public function details() 
    { 
    $user = Auth::user(); 
    return response()->json(['success' => $user], $this-> successStatus); 
    } 

    /**
     * Borrará el token que se haya activado de la cuenta correspondiente.
     * 
     */

    public function logout() {
        
        Auth::user()->tokens->each(function($token, $key) {
            $token->delete();
        });
    
        return response()->json('Successfully logged out');
    }

}
