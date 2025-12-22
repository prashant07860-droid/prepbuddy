import React, { useState } from 'react';
import {
  View,
  Text,
  StyleSheet,
  TextInput,
  TouchableOpacity,
  ActivityIndicator,
  KeyboardAvoidingView,
  Platform,
  ScrollView,
} from 'react-native';
import { useRouter } from 'expo-router';
import { SafeAreaView } from 'react-native-safe-area-context';
import { MaterialCommunityIcons } from '@expo/vector-icons';
import { useAuth } from '../src/AuthContext';

export default function AuthScreen() {
  const router = useRouter();
  const { login, register, continueAsGuest } = useAuth();
  
  const [isLogin, setIsLogin] = useState(true);
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState('');
  const [showPassword, setShowPassword] = useState(false);

  const handleSubmit = async () => {
    setError('');
    
    // Validation
    if (!email || !password) {
      setError('Please fill in all fields');
      return;
    }
    
    if (!isLogin && !name) {
      setError('Please enter your name');
      return;
    }
    
    if (!isLogin && password !== confirmPassword) {
      setError('Passwords do not match');
      return;
    }
    
    if (password.length < 6) {
      setError('Password must be at least 6 characters');
      return;
    }
    
    setIsLoading(true);
    
    try {
      let result;
      if (isLogin) {
        result = await login(email, password);
      } else {
        result = await register(name, email, password);
      }
      
      if (result.success) {
        router.replace('/');
      } else {
        setError(result.error || 'Something went wrong');
      }
    } catch (err) {
      setError('Network error. Please try again.');
    } finally {
      setIsLoading(false);
    }
  };

  const handleGuestMode = () => {
    continueAsGuest();
    router.replace('/');
  };

  return (
    <SafeAreaView style={styles.container}>
      <KeyboardAvoidingView
        behavior={Platform.OS === 'ios' ? 'padding' : 'height'}
        style={styles.keyboardView}
      >
        <ScrollView
          contentContainerStyle={styles.scrollContent}
          showsVerticalScrollIndicator={false}
        >
          {/* Logo and Title */}
          <View style={styles.header}>
            <View style={styles.logoContainer}>
              <MaterialCommunityIcons name="school" size={48} color="#3B82F6" />
            </View>
            <Text style={styles.appTitle}>OPSC Exam Prep</Text>
            <Text style={styles.appSubtitle}>Your path to success</Text>
          </View>

          {/* Auth Form */}
          <View style={styles.formContainer}>
            <Text style={styles.formTitle}>
              {isLogin ? 'Welcome Back!' : 'Create Account'}
            </Text>
            <Text style={styles.formSubtitle}>
              {isLogin
                ? 'Login to track your progress'
                : 'Sign up to save your progress'}
            </Text>

            {error ? (
              <View style={styles.errorContainer}>
                <MaterialCommunityIcons name="alert-circle" size={18} color="#EF4444" />
                <Text style={styles.errorText}>{error}</Text>
              </View>
            ) : null}

            {!isLogin && (
              <View style={styles.inputContainer}>
                <MaterialCommunityIcons name="account" size={20} color="#64748B" style={styles.inputIcon} />
                <TextInput
                  style={styles.input}
                  placeholder="Full Name"
                  placeholderTextColor="#64748B"
                  value={name}
                  onChangeText={setName}
                  autoCapitalize="words"
                />
              </View>
            )}

            <View style={styles.inputContainer}>
              <MaterialCommunityIcons name="email" size={20} color="#64748B" style={styles.inputIcon} />
              <TextInput
                style={styles.input}
                placeholder="Email Address"
                placeholderTextColor="#64748B"
                value={email}
                onChangeText={setEmail}
                keyboardType="email-address"
                autoCapitalize="none"
              />
            </View>

            <View style={styles.inputContainer}>
              <MaterialCommunityIcons name="lock" size={20} color="#64748B" style={styles.inputIcon} />
              <TextInput
                style={styles.input}
                placeholder="Password"
                placeholderTextColor="#64748B"
                value={password}
                onChangeText={setPassword}
                secureTextEntry={!showPassword}
              />
              <TouchableOpacity onPress={() => setShowPassword(!showPassword)}>
                <MaterialCommunityIcons
                  name={showPassword ? 'eye-off' : 'eye'}
                  size={20}
                  color="#64748B"
                />
              </TouchableOpacity>
            </View>

            {!isLogin && (
              <View style={styles.inputContainer}>
                <MaterialCommunityIcons name="lock-check" size={20} color="#64748B" style={styles.inputIcon} />
                <TextInput
                  style={styles.input}
                  placeholder="Confirm Password"
                  placeholderTextColor="#64748B"
                  value={confirmPassword}
                  onChangeText={setConfirmPassword}
                  secureTextEntry={!showPassword}
                />
              </View>
            )}

            {isLogin && (
              <TouchableOpacity
                style={styles.forgotButton}
                onPress={() => router.push('/forgot-password')}
              >
                <Text style={styles.forgotText}>Forgot Password?</Text>
              </TouchableOpacity>
            )}

            <TouchableOpacity
              style={[styles.submitButton, isLoading && styles.submitButtonDisabled]}
              onPress={handleSubmit}
              disabled={isLoading}
            >
              {isLoading ? (
                <ActivityIndicator color="#FFFFFF" />
              ) : (
                <>
                  <MaterialCommunityIcons
                    name={isLogin ? 'login' : 'account-plus'}
                    size={20}
                    color="#FFFFFF"
                  />
                  <Text style={styles.submitButtonText}>
                    {isLogin ? 'Login' : 'Create Account'}
                  </Text>
                </>
              )}
            </TouchableOpacity>

            <TouchableOpacity
              style={styles.switchButton}
              onPress={() => {
                setIsLogin(!isLogin);
                setError('');
              }}
            >
              <Text style={styles.switchText}>
                {isLogin ? "Don't have an account? " : 'Already have an account? '}
                <Text style={styles.switchTextHighlight}>
                  {isLogin ? 'Sign Up' : 'Login'}
                </Text>
              </Text>
            </TouchableOpacity>
          </View>

          {/* Guest Mode */}
          <View style={styles.guestContainer}>
            <View style={styles.dividerContainer}>
              <View style={styles.divider} />
              <Text style={styles.dividerText}>OR</Text>
              <View style={styles.divider} />
            </View>

            <TouchableOpacity style={styles.guestButton} onPress={handleGuestMode}>
              <MaterialCommunityIcons name="account-outline" size={20} color="#94A3B8" />
              <Text style={styles.guestButtonText}>Continue as Guest</Text>
            </TouchableOpacity>
            <Text style={styles.guestNote}>
              Progress won't be saved in guest mode
            </Text>
          </View>
        </ScrollView>
      </KeyboardAvoidingView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#0F172A',
  },
  keyboardView: {
    flex: 1,
  },
  scrollContent: {
    flexGrow: 1,
    padding: 24,
    justifyContent: 'center',
    alignItems: 'center',
  },
  contentWrapper: {
    width: '100%',
    maxWidth: 420,
  },
  header: {
    alignItems: 'center',
    marginBottom: 32,
  },
  logoContainer: {
    width: 80,
    height: 80,
    borderRadius: 20,
    backgroundColor: '#1E293B',
    justifyContent: 'center',
    alignItems: 'center',
    marginBottom: 16,
  },
  appTitle: {
    fontSize: 28,
    fontWeight: '700',
    color: '#F8FAFC',
    marginBottom: 4,
  },
  appSubtitle: {
    fontSize: 16,
    color: '#64748B',
  },
  formContainer: {
    backgroundColor: '#1E293B',
    borderRadius: 20,
    padding: 24,
    marginBottom: 24,
    width: '100%',
  },
  formTitle: {
    fontSize: 22,
    fontWeight: '700',
    color: '#F8FAFC',
    marginBottom: 4,
  },
  formSubtitle: {
    fontSize: 14,
    color: '#94A3B8',
    marginBottom: 24,
  },
  errorContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#450A0A',
    padding: 12,
    borderRadius: 10,
    marginBottom: 16,
  },
  errorText: {
    color: '#FCA5A5',
    fontSize: 14,
    marginLeft: 8,
    flex: 1,
  },
  inputContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#0F172A',
    borderRadius: 12,
    paddingHorizontal: 16,
    marginBottom: 16,
  },
  inputIcon: {
    marginRight: 12,
  },
  input: {
    flex: 1,
    height: 52,
    color: '#F8FAFC',
    fontSize: 16,
  },
  forgotButton: {
    alignSelf: 'flex-end',
    marginBottom: 8,
  },
  forgotText: {
    fontSize: 14,
    color: '#3B82F6',
  },
  submitButton: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: '#3B82F6',
    paddingVertical: 16,
    borderRadius: 12,
    marginTop: 8,
  },
  submitButtonDisabled: {
    opacity: 0.7,
  },
  submitButtonText: {
    fontSize: 16,
    fontWeight: '600',
    color: '#FFFFFF',
    marginLeft: 8,
  },
  switchButton: {
    alignItems: 'center',
    marginTop: 20,
  },
  switchText: {
    fontSize: 14,
    color: '#94A3B8',
  },
  switchTextHighlight: {
    color: '#3B82F6',
    fontWeight: '600',
  },
  guestContainer: {
    alignItems: 'center',
  },
  dividerContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 20,
  },
  divider: {
    flex: 1,
    height: 1,
    backgroundColor: '#334155',
  },
  dividerText: {
    color: '#64748B',
    paddingHorizontal: 16,
    fontSize: 12,
  },
  guestButton: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: '#1E293B',
    paddingVertical: 14,
    paddingHorizontal: 24,
    borderRadius: 12,
    borderWidth: 1,
    borderColor: '#334155',
    width: '100%',
  },
  guestButtonText: {
    fontSize: 15,
    color: '#94A3B8',
    marginLeft: 8,
  },
  guestNote: {
    fontSize: 12,
    color: '#64748B',
    marginTop: 12,
  },
});
