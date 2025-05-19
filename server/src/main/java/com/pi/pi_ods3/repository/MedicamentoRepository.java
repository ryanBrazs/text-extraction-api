package com.pi.pi_ods3.repository;

import java.util.List;

import org.springframework.data.mongodb.repository.MongoRepository;

import com.pi.pi_ods3.models.Medicamento;

public interface MedicamentoRepository extends MongoRepository<Medicamento, String>{
    List<Medicamento> findByNomeContainingIgnoreCase(String nome);
}
