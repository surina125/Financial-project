import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'


export const useSavingStore = defineStore('saving', () => {
  const API_URL = 'http://127.0.0.1:8000'
  const savings = ref([])   // 전체 적금
  const banks = ref([])

  // 가입한 예금 저장
  const contractedSaving = ref([])

  // 관심 예금 저장
  const savedSaving = ref([])
  

  // 전체 데이터 저장
  const getAll = function() {
    axios({
      method: 'get',
      url: `${API_URL}/fin_products/savings/all_bank/all_type/`
    })
      .then(response => {
        savings.value = response.data

        savings.value.forEach(saving => {
          const bankName = saving.kor_co_nm

          // 이미 저장된 은행인지 확인하고 중복되지 않는 경우에만 은행 추가
          if (!banks.value.includes(bankName)) {
            banks.value.push(bankName)
          }

          // 자유적금과 정기적금에 따라 나누어 저장
          if (saving.savingoption_set.rsrv_type_nm === '정액적립식') {
            savingsI.value.push(saving)
          } else if (saving.savingoption_set.rsrv_type_nm === '자유적립식') {
            savingsF.value.push(saving)
          }
        }
      )

      })
      .catch(error => {
        console.log(error)
      })
  }


  return { API_URL, savings, getAll, banks, contractedSaving, savedSaving }
}, { persist: true })
