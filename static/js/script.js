// // Form validation and enhanced interactivity

// document.addEventListener('DOMContentLoaded', function() {
//     // Auto-dismiss alerts after 5 seconds
//     const alerts = document.querySelectorAll('.alert');
//     alerts.forEach(alert => {
//         setTimeout(() => {
//             alert.style.transition = 'opacity 0.5s';
//             alert.style.opacity = '0';
//             setTimeout(() => alert.remove(), 500);
//         }, 5000);
//     });

//     // Password strength indicator
//     const passwordInput = document.querySelector('input[name="password"]');
//     if (passwordInput) {
//         passwordInput.addEventListener('input', function() {
//             const strength = checkPasswordStrength(this.value);
//             const indicator = document.getElementById('password-strength');
//             if (indicator) {
//                 indicator.textContent = strength.text;
//                 indicator.style.color = strength.color;
//             }
//         });
//     }

//     // Confirm password validation
//     const confirmInput = document.querySelector('input[name="confirm_password"]');
//     const pwdInput = document.querySelector('input[name="password"]');
//     if (confirmInput && pwdInput) {
//         confirmInput.addEventListener('input', function() {
//             if (this.value && this.value !== pwdInput.value) {
//                 this.style.borderColor = '#e74c3c';
//                 showError(this, 'Passwords do not match!');
//             } else {
//                 this.style.borderColor = '#27ae60';
//                 hideError(this);
//             }
//         });
//     }

//     // Phone number formatting
//     const phoneInput = document.querySelector('input[name="phone"]');
//     if (phoneInput) {
//         phoneInput.addEventListener('input', function() {
//             this.value = this.value.replace(/[^0-9]/g, '');
//             if (this.value.length > 10) {
//                 this.value = this.value.slice(0, 10);
//             }
//         });
//     }
// });

// // Password strength checker
// function checkPasswordStrength(password) {
//     let strength = 0;
//     const result = { text: '', color: '' };
    
//     if (password.length === 0) {
//         return { text: '', color: '' };
//     }
    
//     if (password.length >= 8) strength++;
//     if (password.match(/[a-z]+/)) strength++;
//     if (password.match(/[A-Z]+/)) strength++;
//     if (password.match(/[0-9]+/)) strength++;
//     if (password.match(/[$@#&!]+/)) strength++;
    
//     switch(strength) {
//         case 0:
//         case 1:
//             result.text = 'Weak';
//             result.color = '#e74c3c';
//             break;
//         case 2:
//         case 3:
//             result.text = 'Medium';
//             result.color = '#f39c12';
//             break;
//         case 4:
//         case 5:
//             result.text = 'Strong';
//             result.color = '#27ae60';
//             break;
//     }
    
//     return result;
// }

// // Show error message
// function showError(element, message) {
//     let error = element.parentElement.querySelector('.error-message');
//     if (!error) {
//         error = document.createElement('small');
//         error.className = 'error-message';
//         error.style.color = '#e74c3c';
//         error.style.fontSize = '12px';
//         error.style.marginTop = '5px';
//         element.parentElement.appendChild(error);
//     }
//     error.textContent = message;
// }

// // Hide error message
// function hideError(element) {
//     const error = element.parentElement.querySelector('.error-message');
//     if (error) {
//         error.remove();
//     }
// }

// // Confirm action
// function confirmAction(message) {
//     return confirm(message || 'Are you sure you want to proceed?');
// }

// // Format currency
// function formatCurrency(amount) {
//     return '₹' + Number(amount).toFixed(0);
// }

// // Get today's date in YYYY-MM-DD format
// function getTodayDate() {
//     const today = new Date();
//     const year = today.getFullYear();
//     const month = String(today.getMonth() + 1).padStart(2, '0');
//     const day = String(today.getDate()).padStart(2, '0');
//     return `${year}-${month}-${day}`;
// }

// // Calculate date difference in days
// function getDateDifference(date1, date2) {
//     const d1 = new Date(date1);
//     const d2 = new Date(date2);
//     const diffTime = Math.abs(d2 - d1);
//     return Math.ceil(diffTime / (1000 * 60 * 60 * 24));
// }

// // Validate email
// function isValidEmail(email) {
//     const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
//     return re.test(email);
// }

// // Validate phone
// function isValidPhone(phone) {
//     return /^[0-9]{10}$/.test(phone);
// }

// // Debounce function for search inputs
// function debounce(func, wait) {
//     let timeout;
//     return function executedFunction(...args) {
//         const later = () => {
//             clearTimeout(timeout);
//             func(...args);
//         };
//         clearTimeout(timeout);
//         timeout = setTimeout(later, wait);
//     };
// }

// // Toast notification
// function showToast(message, type = 'success') {
//     const colors = {
//         success: '#27ae60',
//         error: '#e74c3c',
//         warning: '#f39c12',
//         info: '#3498db'
//     };
    
//     const toast = document.createElement('div');
//     toast.style.cssText = `
//         position: fixed;
//         top: 20px;
//         right: 20px;
//         padding: 15px 25px;
//         background: ${colors[type] || '#333'};
//         color: white;
//         border-radius: 10px;
//         box-shadow: 0 4px 15px rgba(0,0,0,0.2);
//         z-index: 9999;
//         animation: slideIn 0.5s ease;
//         max-width: 400px;
//     `;
//     toast.textContent = message;
//     document.body.appendChild(toast);
    
//     setTimeout(() => {
//         toast.style.opacity = '0';
//         toast.style.transition = 'opacity 0.5s';
//         setTimeout(() => toast.remove(), 500);
//     }, 4000);
// }

// // Add slideIn animation
// const style = document.createElement('style');
// style.textContent = `
//     @keyframes slideIn {
//         from {
//             transform: translateX(100px);
//             opacity: 0;
//         }
//         to {
//             transform: translateX(0);
//             opacity: 1;
//         }
//     }
// `;
// document.head.appendChild(style);

// // Export functions for use in other scripts
// window.showToast = showToast;
// window.confirmAction = confirmAction;
// window.formatCurrency = formatCurrency;
// window.getTodayDate = getTodayDate;
// window.isValidEmail = isValidEmail;
// window.isValidPhone = isValidPhone;




// Auto-dismiss alerts after 5 seconds
document.addEventListener('DOMContentLoaded', function() {
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            alert.style.transition = 'opacity 0.5s';
            alert.style.opacity = '0';
            setTimeout(() => alert.remove(), 500);
        }, 5000);
    });
});

// Confirm action
function confirmAction(message) {
    return confirm(message || 'Are you sure you want to proceed?');
}