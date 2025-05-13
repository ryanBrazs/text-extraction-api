package com.pi.pi_ods3.repository;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;

import com.pi.pi_ods3.models.Medicamento;

public interface MedicamentoRepository extends JpaRepository<Medicamento, Long>{
    List<Medicamento> findByNomeContainingIgnoreCase(String nome);
}
