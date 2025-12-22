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
import Constants from 'expo-constants';

const getBackendUrl = () => {
  return Constants.expoConfig?.extra?.EXPO_PUBLIC_BACKEND_URL 
    || process.env.EXPO_PUBLIC_BACKEND_URL 
    || '';
};

type Step = 'email' | 'code' | 'newPassword' | 'success';

export default function ForgotPasswordScreen() {
  const router = useRouter();
  
  const [step, setStep] = useState<Step>('email');
  const [email, setEmail] = useState('');
  const [resetCode, setResetCode] = useState('');
  const [newPassword, setNewPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState('');
  const [showPassword, setShowPassword] = useState(false);
  const [generatedCode, setGeneratedCode] = useState('');

  const handleRequestCode = async () => {
    setError('');
    
    if (!email) {
      setError('Please enter your email address');
      return;
    }
    
    setIsLoading(true);
    
    try {
      const backendUrl = getBackendUrl();
      const response = await fetch(`${backendUrl}/api/auth/forgot-password`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ email }),
      });

      const data = await response.json();

      if (response.ok) {
        // For testing, show the code (in production, remove this)
        if (data.reset_code) {
          setGeneratedCode(data.reset_code);
        }
        setStep('code');
      } else {
        setError(data.detail || 'Failed to send reset code');
      }
    } catch (err) {
      setError('Network error. Please try again.');
    } finally {
      setIsLoading(false);
    }
  };

  const handleVerifyCode = () => {
    setError('');
    
    if (!resetCode || resetCode.length !== 6) {
      setError('Please enter the 6-digit code');
      return;
    }
    
    setStep('newPassword');
  };

  const handleResetPassword = async () => {
    setError('');
    
    if (!newPassword) {
      setError('Please enter a new password');
      return;
    }
    
    if (newPassword.length < 6) {
      setError('Password must be at least 6 characters');
      return;
    }
    
    if (newPassword !== confirmPassword) {
      setError('Passwords do not match');
      return;
    }
    
    setIsLoading(true);
    
    try {
      const backendUrl = getBackendUrl();
      const response = await fetch(`${backendUrl}/api/auth/reset-password`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          email,
          reset_code: resetCode,
          new_password: newPassword,
        }),
      });

      const data = await response.json();

      if (response.ok) {
        setStep('success');
      } else {
        setError(data.detail || 'Failed to reset password');
      }
    } catch (err) {
      setError('Network error. Please try again.');
    } finally {
      setIsLoading(false);
    }
  };

  const renderEmailStep = () => (
    <>
      <Text style={styles.stepTitle}>Forgot Password?</Text>
      <Text style={styles.stepDescription}>
        Enter your email address and we'll send you a reset code.
      </Text>

      {error ? (
        <View style={styles.errorContainer}>
          <MaterialCommunityIcons name="alert-circle" size={18} color="#EF4444" />
          <Text style={styles.errorText}>{error}</Text>
        </View>
      ) : null}

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

      <TouchableOpacity
        style={[styles.submitButton, isLoading && styles.submitButtonDisabled]}
        onPress={handleRequestCode}
        disabled={isLoading}
      >
        {isLoading ? (
          <ActivityIndicator color="#FFFFFF" />
        ) : (
          <>
            <MaterialCommunityIcons name="send" size={20} color="#FFFFFF" />
            <Text style={styles.submitButtonText}>Send Reset Code</Text>
          </>
        )}
      </TouchableOpacity>
    </>
  );

  const renderCodeStep = () => (
    <>
      <Text style={styles.stepTitle}>Enter Reset Code</Text>
      <Text style={styles.stepDescription}>
        Enter the 6-digit code sent to {email}
      </Text>

      {/* For testing - show the generated code */}
      {generatedCode ? (
        <View style={styles.codePreview}>
          <MaterialCommunityIcons name="information" size={18} color="#3B82F6" />
          <Text style={styles.codePreviewText}>
            Your code: <Text style={styles.codePreviewCode}>{generatedCode}</Text>
          </Text>
        </View>
      ) : null}

      {error ? (
        <View style={styles.errorContainer}>
          <MaterialCommunityIcons name="alert-circle" size={18} color="#EF4444" />
          <Text style={styles.errorText}>{error}</Text>
        </View>
      ) : null}

      <View style={styles.inputContainer}>
        <MaterialCommunityIcons name="numeric" size={20} color="#64748B" style={styles.inputIcon} />
        <TextInput
          style={[styles.input, styles.codeInput]}
          placeholder="000000"
          placeholderTextColor="#64748B"
          value={resetCode}
          onChangeText={(text) => setResetCode(text.replace(/[^0-9]/g, '').slice(0, 6))}
          keyboardType="number-pad"
          maxLength={6}
        />
      </View>

      <TouchableOpacity
        style={styles.submitButton}
        onPress={handleVerifyCode}
      >
        <MaterialCommunityIcons name="check" size={20} color="#FFFFFF" />
        <Text style={styles.submitButtonText}>Verify Code</Text>
      </TouchableOpacity>

      <TouchableOpacity
        style={styles.resendButton}
        onPress={handleRequestCode}
      >
        <Text style={styles.resendText}>Didn't receive code? Resend</Text>
      </TouchableOpacity>
    </>
  );

  const renderNewPasswordStep = () => (
    <>
      <Text style={styles.stepTitle}>Set New Password</Text>
      <Text style={styles.stepDescription}>
        Create a new password for your account
      </Text>

      {error ? (
        <View style={styles.errorContainer}>
          <MaterialCommunityIcons name="alert-circle" size={18} color="#EF4444" />
          <Text style={styles.errorText}>{error}</Text>
        </View>
      ) : null}

      <View style={styles.inputContainer}>
        <MaterialCommunityIcons name="lock" size={20} color="#64748B" style={styles.inputIcon} />
        <TextInput
          style={styles.input}
          placeholder="New Password"
          placeholderTextColor="#64748B"
          value={newPassword}
          onChangeText={setNewPassword}
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

      <View style={styles.inputContainer}>
        <MaterialCommunityIcons name="lock-check" size={20} color="#64748B" style={styles.inputIcon} />
        <TextInput
          style={styles.input}
          placeholder="Confirm New Password"
          placeholderTextColor="#64748B"
          value={confirmPassword}
          onChangeText={setConfirmPassword}
          secureTextEntry={!showPassword}
        />
      </View>

      <TouchableOpacity
        style={[styles.submitButton, isLoading && styles.submitButtonDisabled]}
        onPress={handleResetPassword}
        disabled={isLoading}
      >
        {isLoading ? (
          <ActivityIndicator color="#FFFFFF" />
        ) : (
          <>
            <MaterialCommunityIcons name="lock-reset" size={20} color="#FFFFFF" />
            <Text style={styles.submitButtonText}>Reset Password</Text>
          </>
        )}
      </TouchableOpacity>
    </>
  );

  const renderSuccessStep = () => (
    <View style={styles.successContainer}>
      <View style={styles.successIcon}>
        <MaterialCommunityIcons name="check-circle" size={64} color="#22C55E" />
      </View>
      <Text style={styles.successTitle}>Password Reset!</Text>
      <Text style={styles.successDescription}>
        Your password has been successfully reset. You can now login with your new password.
      </Text>
      <TouchableOpacity
        style={styles.submitButton}
        onPress={() => router.replace('/auth')}
      >
        <MaterialCommunityIcons name="login" size={20} color="#FFFFFF" />
        <Text style={styles.submitButtonText}>Go to Login</Text>
      </TouchableOpacity>
    </View>
  );

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
          {/* Back Button */}
          <TouchableOpacity
            style={styles.backButton}
            onPress={() => {
              if (step === 'email') {
                router.back();
              } else if (step === 'code') {
                setStep('email');
              } else if (step === 'newPassword') {
                setStep('code');
              }
            }}
          >
            <MaterialCommunityIcons name="arrow-left" size={24} color="#F8FAFC" />
          </TouchableOpacity>

          {/* Progress Indicator */}
          {step !== 'success' && (
            <View style={styles.progressContainer}>
              <View style={[styles.progressDot, step === 'email' && styles.progressDotActive]} />
              <View style={styles.progressLine} />
              <View style={[styles.progressDot, step === 'code' && styles.progressDotActive]} />
              <View style={styles.progressLine} />
              <View style={[styles.progressDot, step === 'newPassword' && styles.progressDotActive]} />
            </View>
          )}

          {/* Form Container */}
          <View style={styles.formContainer}>
            {step === 'email' && renderEmailStep()}
            {step === 'code' && renderCodeStep()}
            {step === 'newPassword' && renderNewPasswordStep()}
            {step === 'success' && renderSuccessStep()}
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
  },
  backButton: {
    width: 44,
    height: 44,
    borderRadius: 12,
    backgroundColor: '#1E293B',
    justifyContent: 'center',
    alignItems: 'center',
    marginBottom: 24,
  },
  progressContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    marginBottom: 32,
  },
  progressDot: {
    width: 12,
    height: 12,
    borderRadius: 6,
    backgroundColor: '#334155',
  },
  progressDotActive: {
    backgroundColor: '#3B82F6',
  },
  progressLine: {
    width: 40,
    height: 2,
    backgroundColor: '#334155',
    marginHorizontal: 8,
  },
  formContainer: {
    backgroundColor: '#1E293B',
    borderRadius: 20,
    padding: 24,
  },
  stepTitle: {
    fontSize: 24,
    fontWeight: '700',
    color: '#F8FAFC',
    marginBottom: 8,
  },
  stepDescription: {
    fontSize: 14,
    color: '#94A3B8',
    marginBottom: 24,
    lineHeight: 20,
  },
  codePreview: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#1E3A5F',
    padding: 12,
    borderRadius: 10,
    marginBottom: 16,
  },
  codePreviewText: {
    color: '#94A3B8',
    fontSize: 14,
    marginLeft: 8,
  },
  codePreviewCode: {
    color: '#3B82F6',
    fontWeight: '700',
    fontSize: 16,
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
  codeInput: {
    fontSize: 24,
    fontWeight: '600',
    letterSpacing: 8,
    textAlign: 'center',
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
  resendButton: {
    alignItems: 'center',
    marginTop: 20,
  },
  resendText: {
    fontSize: 14,
    color: '#3B82F6',
  },
  successContainer: {
    alignItems: 'center',
    paddingVertical: 20,
  },
  successIcon: {
    marginBottom: 20,
  },
  successTitle: {
    fontSize: 24,
    fontWeight: '700',
    color: '#F8FAFC',
    marginBottom: 12,
  },
  successDescription: {
    fontSize: 14,
    color: '#94A3B8',
    textAlign: 'center',
    marginBottom: 32,
    lineHeight: 20,
  },
});
